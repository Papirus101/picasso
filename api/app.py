from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.police import police_router
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI(
        docs_url='/api/docs',
        redoc_url='/api/redoc',
        openapi_url='/api/openapi.json'
        )

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(police_router, prefix='/api')
