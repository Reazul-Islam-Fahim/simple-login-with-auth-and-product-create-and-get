from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import timedelta
from schemas import UserLogin
from database import SessionLocal, get_db
from models import User
from auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login", summary="Login with username and password")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = create_access_token(
        data={"sub": db_user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
