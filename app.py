from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}

app.on_event("startup")
async def startup():
    print("Startup")

app.on_event("shutdown")
async def shutdown():
    print("Shutdown")    