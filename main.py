from fastapi import FastAPI 

app = FastAPI(title="API do Noan")

@app.get("/")
def helloWorld():
    return{"message": "Hello World!"}