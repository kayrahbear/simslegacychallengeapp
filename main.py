from fastapi import FastAPI
from legacyDB.user import router as user_router

app = FastAPI(title="LegacyDB", version="0.0.1")

app.include_router(user_router.router)
