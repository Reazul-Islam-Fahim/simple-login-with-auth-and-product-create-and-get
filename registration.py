from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import UserRegister
from datetime import timedelta
from database import SessionLocal, get_db
from models import User
from auth import hash_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/register", summary="Register a new user")
def register_user(user: UserRegister, db: Session = Depends(get_db)):

    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    token = create_access_token(
        data={"sub": db_user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "message": "User registered successfully",
        "access_token": token,
        "token_type": "bearer"
    }
