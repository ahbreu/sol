import argparse
import sys
import time
import threading
import itertools
import random

from core.config_loader import carregar_config
from core.carregar_modelo import carregar_modelo
from core.processar_input import processar_input
from core.gerar_resposta import gerar_resposta_modelo
from core.logger import salvar_conversa
from core.gerar_prompt import montar_prompt
from core.validador import entrada_valida

# Emoções possíveis para deixar o chat mais humano
EMOCOES = ["😎", "😅", "💬", "✨", "🥰", "🤖", "🔥", "🌟", "🧠", "🎶", "🚀"]

# Carregar configuração
config = carregar_config()
CAMINHO_MODELO = config.get("caminho_modelo", "modelo/modelo.gguf")
CAMINHO_CONTEXTO = config.get("caminho_contexto", "memoria/contexto.md")

# Argumentos CLI
parser = argparse.ArgumentParser(description="Executa a IA Sol localmente.")
parser.add_argument("--debug", action="store_true", help="Ativa modo debug com mensagens extras")
parser.add_argument("--voz", action="store_true", help="Modo de voz (futuro)")
parser.add_argument("--offline", action="store_true", help="Executa em modo offline (simulado)")
args = parser.parse_args()

# Função de animação "Sol está digitando..."
def animar_digitando():
    anima = "|/-\\"
    idx = 0
    while not parar_animacao:
        print(f"\rSol está digitando... {anima[idx % len(anima)]}", end="")
        idx += 1
        time.sleep(0.1)
    print("\r", end="")  # Limpa linha final

# Carregar o modelo
try:
    modelo = carregar_modelo(CAMINHO_MODELO)
except FileNotFoundError as e:
    print(f"[ERRO] {e}")
    print("[Sol] Não consegui carregar meu cérebro, Pê... 🧠💤")
    exit()

# Mensagens iniciais
if args.voz:
    print("[Sol] Modo voz ativado. Ainda não implementado, mas já tô ouvindo, hein 😎")
if args.offline:
    print("[Sol] Sem internet, mas contigo até no modo avião. ✈️💛")

# Loop de conversa
while True:
    user_input = input("Pê diz: ")

    if not entrada_valida(user_input):
        print("Sol diz: Pê... tu não disse nada. Bora conversar sério. 😅")
        continue
    
    if user_input.strip().lower() == "/sair":
        print("[Sol] Tá bom... Mas volta logo, tá? 🌙💛")
        break

    entrada = processar_input(user_input)

    if args.debug:
        print(f"[DEBUG] Entrada processada: {entrada}")

    prompt = montar_prompt(CAMINHO_CONTEXTO, entrada)

    # Animação enquanto gera a resposta
    parar_animacao = False
    animacao = threading.Thread(target=animar_digitando)
    animacao.start()

    try:
        resposta = gerar_resposta_modelo(modelo, prompt)
    except Exception as e:
        parar_animacao = True
        animacao.join()
        print(f"\n[Sol] Erro ao tentar pensar: {e}")
        continue

    parar_animacao = True
    animacao.join()

    # Exibe resposta com emoção aleatória
    emoji = random.choice(EMOCOES)
    print(f"\nSol diz {emoji}: {resposta}")

    salvar_conversa(user_input, resposta, emoji)