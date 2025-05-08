import os
from pathlib import Path
from llama_cpp import Llama

# Definindo o número de threads para otimização
os.environ["OMP_NUM_THREADS"] = "8"  # Forçando 8 threads do i7
os.environ["MKL_NUM_THREADS"] = "8"
os.environ["NUMEXPR_NUM_THREADS"] = "8"
os.environ["OPENBLAS_NUM_THREADS"] = "8"

# Caminho absoluto do modelo
caminho_modelo = Path(__file__).resolve().parent.parent / 'modelo' / 'modelo.gguf'

def carregar_modelo(caminho_modelo):
    try:
        print(f"[Sol] Carregando modelo de: {caminho_modelo}")
        modelo = Llama(
            model_path=str(caminho_modelo),
            n_ctx=2048,
            n_threads=8
        )
        print("[Sol] Modelo carregado com sucesso! 🚀")
        return modelo
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar modelo: {e}")

modelo = carregar_modelo(caminho_modelo)
