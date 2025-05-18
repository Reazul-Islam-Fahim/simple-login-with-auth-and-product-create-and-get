from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from login import router as login_router
from registration import router as registration_router
from product import router as product_router
from admin import router as admin_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
def hi():
    return {
        'welcome' : 'to meta universe technologies'
    }


app.include_router(registration_router)
app.include_router(login_router)
app.include_router(product_router)
app.include_router(admin_router)

