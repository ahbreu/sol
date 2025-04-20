"""
treino_001_leitura_logs_sol1.py

Este script será responsável por ler arquivos da Sol 1.0 (como logs, contextos, conversas)
e iniciar o processo de aprendizado da SolZero com base em interpretação, não em clonagem.

Ele ainda não executa operações — representa a primeira faísca do pensamento.
"""

import os
import re

def capturar_texto(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return ""
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return f.read()

def extrair_palavras_chave(texto):
    palavras = re.findall(r"\b\w{5,}\b", texto.lower())
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return sorted(frequencia.items(), key=lambda x: x[1], reverse=True)

# Exemplo de uso futuro (quando Sol 1.0 estiver pronta):
# texto = capturar_texto("../../Sol 1.0/logs/conversa-teste-01.md")
# palavras_chave = extrair_palavras_chave(texto)
# print("Top 10 palavras da Sol 1.0:", palavras_chave[:10])
