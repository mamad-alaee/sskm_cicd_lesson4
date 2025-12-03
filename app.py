from fastapi import FastAPI,HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# soheil injas
@app.get("/error")
def response_error():
    raise HTTPException(
        status_code=401,
        detail="Item not found")
    