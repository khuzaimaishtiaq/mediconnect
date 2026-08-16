from pydantic import BaseModel, EmailStr
from typing import Optional, List

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: str = "patient" # patient or doctor

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AppointmentRequest(BaseModel):
    doctor_id: str
    date: str
    time: str
    type: str # 'video' or 'in-person'
    symptoms: Optional[str] = None
