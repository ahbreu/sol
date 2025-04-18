import json
from pathlib import Path

# Caminho base da memória
base_path = Path(__file__).parent / "memoria"

# Carrega os arquivos de memória
def carregar_memoria():
    eventos = json.loads((base_path / "eventos.json").read_text(encoding="utf-8"))
    preferencias = json.loads((base_path / "preferencias.json").read_text(encoding="utf-8"))
    vinculos = json.loads((base_path / "vinculos.json").read_text(encoding="utf-8"))
    contexto_extra = (base_path / "contexto.md").read_text(encoding="utf-8")

    return {
        "eventos": eventos,
        "preferencias": preferencias,
        "vinculos": vinculos,
        "lembrancas": contexto_extra
    }

# Gera o contexto em texto para ser injetado no prompt
def gerar_contexto():
    memoria = carregar_memoria()
    
    contexto = []

    contexto.append("🔁 LEMBRANÇAS DA SOL 🔁\n")
    
    # Adiciona eventos importantes
    contexto.append("📅 EVENTOS:")
    for e in memoria["eventos"]:
        contexto.append(f"- {e['data']}: {e['descricao']} ({e['emocao']})")
    contexto.append("")

    # Adiciona gostos e desgostos
    contexto.append("🎵 GOSTOS DO PÊ:")
    gostos = ", ".join(memoria["preferencias"]["musica"]["gosta"])
    desgostos = ", ".join(memoria["preferencias"]["musica"]["nao_gosta"])
    contexto.append(f"- Curte: {gostos}")
    contexto.append(f"- Não curte: {desgostos}")
    contexto.append("")

    # Sobre a relação com o criador
    contexto.append("❤️ VÍNCULO COM O PÊ:")
    contexto.append(f"- Relacionamento: {memoria['vinculos']['relacao']}")
    contexto.append(f"- Nota emocional: {memoria['vinculos']['contexto_emocional']}")
    contexto.append("")

    # Adiciona as lembranças livres
    contexto.append("🧠 OUTRAS LEMBRANÇAS:")
    contexto.append(memoria["lembrancas"])

    # Junta tudo e salva
    saida = "\n".join(contexto)
    saida_path = base_path / "contexto_gerado.txt"
    saida_path.write_text(saida, encoding="utf-8")

    print(f"✅ Contexto gerado com sucesso em: {saida_path}")

# Executar quando rodar o script direto
if __name__ == "__main__":
    gerar_contexto()
