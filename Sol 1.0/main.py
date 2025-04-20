import argparse
from core.carregar_modelo import carregar_modelo
from core.processar_input import processar_input
from core.gerar_resposta import gerar_resposta
from core.logger import salvar_conversa
from core.gerar_prompt import montar_prompt

# Argumentos de execução
parser = argparse.ArgumentParser(description="Executa a IA Sol localmente.")
parser.add_argument("--debug", action="store_true", help="Ativa modo debug com mensagens extras")
parser.add_argument("--voz", action="store_true", help="Modo de voz (futuro)")
parser.add_argument("--offline", action="store_true", help="Executa em modo offline (simulado)")
args = parser.parse_args()

# Caminhos
CAMINHO_MODELO = "modelo/modelo.gguf"
CAMINHO_CONTEXTO = "memoria/contexto.md"

# Carregamento do modelo
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
    
    if user_input.strip().lower() == "/sair":
        print("[Sol] Tá bom... Mas volta logo, tá? 🌙💛")
        break

    entrada = processar_input(user_input)

    if args.debug:
        print(f"[DEBUG] Entrada processada: {entrada}")

    prompt = montar_prompt(CAMINHO_CONTEXTO, entrada)
    resposta = gerar_resposta(modelo, prompt)

    print(f"Sol diz: {resposta}")
    salvar_conversa(user_input, resposta)
