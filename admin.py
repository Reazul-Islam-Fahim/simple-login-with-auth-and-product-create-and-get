from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import RoleUpdate, UserOut

router = APIRouter()

@router.post("/manage_role", response_model=UserOut)
def manage_role(role_data: RoleUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == role_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = role_data.role
    db.commit()
    db.refresh(user)
    return user
