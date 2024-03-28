from fastapi.middleware.cors import CORSMiddleware
from controller import router
from fastapi import FastAPI
from decouple import config


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config('CORS_ALLOWED')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

#uvicorn main:app iniciar o servidor
# EX: uvicorn main:app --host 0.0.0.0 --port 8002
