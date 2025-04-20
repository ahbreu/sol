import os
from pathlib import Path

def carregar_modelo(caminho_modelo):
    if not Path(caminho_modelo).exists():
        raise FileNotFoundError(f"Modelo não encontrado: {caminho_modelo}")
    
    print(f"[Sol] Carregando modelo: {caminho_modelo}")
    # No futuro: integração com llama.cpp ou inferência Python aqui
    return f"Modelo simulado carregado de {caminho_modelo}"
