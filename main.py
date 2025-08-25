from fastapi import FastAPI

app = FastAPI(title="API")



@app.get("/")
def helloWorld():
    return {"message": "Hello World"}

@app.get("/aluno")
def get_aluno():
    return{"insira na rota após o "/" o nome do aluno"}

@app.get("/aluno/{nome-aluno}")
def get_aluno_by_name(nome_aluno: str):
    return("O nome do aluno é:", nome_aluno)

