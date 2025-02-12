from fastapi import FastAPI
from routers import contact

app = FastAPI()

# @app.get("/")
# async def root():
#     return { "message" : "hello world" }

app.include_router(contact.router)