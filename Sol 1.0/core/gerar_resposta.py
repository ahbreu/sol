def gerar_resposta_modelo(modelo, prompt):
    try:
        resultado = modelo(
            prompt=prompt,
            max_tokens=512,  # quantos tokens ela gera no máximo
            temperature=0.7, # mais alto = mais criativo, mais baixo = mais preciso
            stop=["Pê:", "Sol:", "\n\n"]  # parar em delimitações pra evitar loop
        )
        resposta = resultado['choices'][0]['text'].strip()

        # Corta resposta se ainda sobrar lixo
        resposta = resposta.split("Pê:")[0].split("Sol:")[0].strip()

        return resposta
    except Exception as e:
        return f"[Sol] Tive um errinho ao pensar: {e}"

