from core.carregar_modelo import modelo

def gerar_resposta(prompt, max_tokens=512, temperatura=0.7):
    """
    Gera a resposta do modelo com controle de fluxo para evitar loops infinitos e repetições.
    
    Parâmetros:
    - prompt (str): Pergunta ou mensagem enviada para a Sol.
    - max_tokens (int): Quantidade máxima de tokens gerados.
    - temperatura (float): Controle de criatividade do modelo.
    
    Retorno:
    - (str): Resposta gerada pela Sol.
    """
    print("🔄 Sol está pensando...")

    resposta_final = ""
    contador_tokens = 0
    loop_detection = set()  # Guarda as últimas frases para detectar loops

    try:
        # 🌀 **STREAMING ATIVO:** A Sol vai respondendo enquanto gera
        for token in modelo.stream_chat(prompt, max_tokens=max_tokens, temperature=temperatura):
            print(token, end='', flush=True)
            resposta_final += token
            contador_tokens += 1

            # Detecção de loop: se o token já foi gerado recentemente, corta
            if token in loop_detection:
                print("\n⚠️ Loop detectado, interrompendo resposta para não travar.")
                break
            else:
                loop_detection.add(token)
            
            # Evita que o set cresça infinitamente
            if len(loop_detection) > 20:
                loop_detection.pop()

            # Verificação de limite de tokens
            if contador_tokens >= max_tokens:
                print("\n⚠️ Limite de tokens atingido, resposta finalizada.")
                break

        print("\n✅ Resposta completa.")
        return resposta_final.strip()
    
    except Exception as e:
        print(f"\n[Sol] Tive um errinho ao pensar: {e}")
        return f"[Sol] Tive um errinho ao pensar: {e}"
