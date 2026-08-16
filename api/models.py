from pydantic import BaseModel
from typing import Optional, List

class SignupRequest(BaseModel):
    username: str
    password: str
    name: str
    role: str = "patient" # patient or doctor

class LoginRequest(BaseModel):
    username: str
    password: str

class AppointmentRequest(BaseModel):
    doctor_id: str
    date: str
    time: str
    type: str # 'video' or 'in-person'
    symptoms: Optional[str] = None
