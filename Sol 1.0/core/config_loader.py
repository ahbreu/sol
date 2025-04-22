import json

def carregar_config(caminho="core/config.json"):
    """
    Carrega as configurações do sistema a partir do JSON.
    """
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("[Sol] Arquivo de configuração não encontrado!")
        return {}
    except json.JSONDecodeError:
        print("[Sol] Erro ao ler o arquivo de configuração (formato inválido).")
        return {}
