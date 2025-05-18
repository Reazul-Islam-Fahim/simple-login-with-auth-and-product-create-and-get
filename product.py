from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
import models
import schemas
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.get("/products/", response_model=list[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    try:
        products = db.query(models.Product).all()
        return products
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
    

@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    try:
        db_product = models.Product(
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity
        )
        
        db.add(db_product)
        db.commit()
        db.refresh(db_product) 
        
        return db_product 
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail="Database error occurred")

