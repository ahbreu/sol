"""
logger.py

Função: salvar_conversa
Responsável por criar e atualizar um log de conversa entre o Pê e a Sol 1.0.

Cada linha salva terá timestamp e será formatada em Markdown para leitura futura.
O arquivo de log será salvo na pasta /logs/ com o nome: conversa-YYYY-MM-DD_HHMM.md
"""

from datetime import datetime
from pathlib import Path

# Garante que a pasta 'logs/' existe
Path("logs").mkdir(parents=True, exist_ok=True)

# Nome do arquivo baseado na hora de início
datahora = datetime.now().strftime("%Y-%m-%d_%H%M")
arquivo_log = Path(f"logs/conversa-{datahora}.md")

# Cria o arquivo de log e adiciona o cabeçalho, se ainda não existir
if not arquivo_log.exists():
    with open(arquivo_log, "w", encoding="utf-8") as f:
        f.write(f"# 🧠 Conversa com Sol – {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n\n")

def salvar_conversa(user_input, resposta, emocao="🤖"):
    with open("logs/conversa-log.txt", "a", encoding="utf-8") as log:
        log.write(f"[Pê]: {user_input}\n")
        log.write(f"[Sol] ({emocao}): {resposta}\n\n")
