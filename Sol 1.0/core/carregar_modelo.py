from  import Llama

def carregar_modelo(caminho_modelo):
    try:
        modelo = Llama(
            model_path=caminho_modelo,
            n_ctx=2048,  # tamanho do contexto (ajustável)
            n_threads=8  # threads da CPU (pode aumentar pra 6-8 no seu i7)
        )
        print("[Sol] Modelo carregado com sucesso! 🚀")
        return modelo
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar modelo: {e}")
