from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.user import router  as user_router

app = FastAPI(
    title="MediaApp API",
    description="API for MediaApp application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to MediaApp API"}

app.include_router(user_router)