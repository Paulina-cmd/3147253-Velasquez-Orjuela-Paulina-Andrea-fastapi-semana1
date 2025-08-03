from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola Mundo desde FastAPI!"}

@app.get("/saludo")
def saludo(nombre: str = "Estudiante"):
    return {"saludo": f"Hola, {nombre}. ¡Bienvenido a FastAPI!"}
