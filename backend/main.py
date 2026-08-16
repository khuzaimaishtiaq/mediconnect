from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from db import supabase
from models import SignupRequest, LoginRequest, AppointmentRequest
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="MediConnect App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
@app.post("/api/auth/signup")
def signup(req: SignupRequest):
    res = supabase.auth.sign_up({
        "email": req.email,
        "password": req.password,
        "options": {"data": {"name": req.name, "role": req.role}}
    })
    
    if not res.user:
        raise HTTPException(status_code=400, detail="Signup failed.")
    
    # Store additionally in profiles
    supabase.table("profiles").insert({
        "id": res.user.id,
        "name": req.name,
        "email": req.email,
        "role": req.role
    }).execute()

    return {"access_token": res.session.access_token, "user": res.user}

@app.post("/api/auth/login")
def login(req: LoginRequest):
    res = supabase.auth.sign_in_with_password({
        "email": req.email,
        "password": req.password
    })
    if not res.session:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    # Get profile
    profile = supabase.table("profiles").select("*").eq("id", res.user.id).single().execute()
    
    return {
        "access_token": res.session.access_token,
        "user": res.user,
        "profile": profile.data
    }

@app.get("/api/doctors")
def get_doctors(specialty: str = None):
    query = supabase.table("profiles").select("*").eq("role", "doctor")
    if specialty:
        # Assuming doctors have a specialty column in profiles
        # For simplicity, we just fetch all and filter in frontend if not in table
        pass
    res = query.execute()
    return res.data

@app.post("/api/appointments")
def book_appointment(req: AppointmentRequest):
    # Depending on auth context, user_id should be extracted from headers
    # For simplicity of this demo, we assume the user is authenticated in frontend and passes info
    # In a real app we'd verify the JWT
    res = supabase.table("appointments").insert({
        "doctor_id": req.doctor_id,
        "date": req.date,
        "time": req.time,
        "type": req.type,
        "symptoms": req.symptoms
    }).execute()
    return res.data

@app.get("/api/appointments")
def get_appointments(user_id: str):
    # For a patient
    res = supabase.table("appointments").select("*").eq("patient_id", user_id).execute()
    return res.data

# Frontend routes
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/{full_path:path}")
def serve_spa(full_path: str):
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
