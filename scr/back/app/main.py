from fastapi import FastAPI
from app.routers import tasks, users
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(tasks.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Ferramenta de Gestão de Procrastinação!"}



# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos os domínios; ajuste conforme necessário
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

