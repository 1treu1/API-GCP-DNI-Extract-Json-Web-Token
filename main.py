from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.users_ocr import users_ocr
app = FastAPI()

app.include_router(auth_routes, prefix="/api")
app.include_router(users_ocr, prefix="/api")
load_dotenv()