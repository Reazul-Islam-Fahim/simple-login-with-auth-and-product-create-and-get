from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
     
    class Config:
        orm_mode = True  

class UserLogin(BaseModel):
    username: str
    password: str
     
    class Config:
        orm_mode = True  

class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: Optional[int] = 0
     
    class Config:
        orm_mode = True  
        
class RoleUpdate(BaseModel):
    username: str
    role: str

    @validator("role")
    def validate_role(cls, v):
        if v not in ("admin", "user"):
            raise ValueError("Role must be 'admin' or 'user'")
        return v

class UserOut(BaseModel):
    username: str
    email: str
    role: str

    class Config:
        orm_mode = True

