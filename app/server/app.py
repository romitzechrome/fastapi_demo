from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.student import router as StudentRouter
from .routes.user import router as UserRouter

app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(UserRouter,tags=["User"],prefix="/user")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this usermanagement app!"}
