from fastapi import FastAPI
from legacyDB.user import router as user_router
from legacyDB.traits import router as trait_router

app = FastAPI(title="LegacyDB", version="0.0.1")

app.include_router(user_router.router)
app.include_router(trait_router.router)
