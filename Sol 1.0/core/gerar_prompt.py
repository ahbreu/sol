"""
gerar_prompt.py

Função: montar_prompt
Lê o contexto.md da memória da Sol 1.0 e junta com a entrada do usuário,
gerando o prompt final que será enviado ao modelo.

Isso dá "alma" e personalidade à Sol, pois ela responde com base no que sabe sobre o Pê.
"""

def montar_prompt(caminho_contexto, entrada_usuario):
    try:
        with open(caminho_contexto, "r", encoding="utf-8") as f:
            contexto = f.read()
    except FileNotFoundError:
        contexto = "[Sem contexto carregado]\n"

    prompt_final = f"""{contexto}

Pê: {entrada_usuario}
Sol:"""
    return prompt_final
