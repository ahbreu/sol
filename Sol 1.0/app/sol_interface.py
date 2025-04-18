import streamlit as st
from pathlib import Path

# === CONFIGURAÇÃO INICIAL ===
st.set_page_config(page_title="Sol – IA Local do Pê", page_icon="☀️")
st.title("🌞 Sol – sua IA local, com memória e alma")

# === CAMINHO DO CONTEXTO ===
contexto_path = Path(__file__).parent.parent / "memoria" / "contexto_gerado.txt"

# === MOSTRA O CONTEXTO ATUAL ===
with st.expander("🔁 Ver memória atual da Sol"):
    if contexto_path.exists():
        contexto = contexto_path.read_text(encoding="utf-8")
        st.text_area("🧠 Contexto carregado:", contexto, height=300)
    else:
        st.warning("Ainda não há contexto gerado. Rode o memoria_sol.py primeiro.")

# === ENTRADA DE CONVERSA ===
st.markdown("---")
st.subheader("🗣️ Fale com a Sol")

mensagem = st.text_input("O que você quer dizer pra mim, Pê?")

if mensagem:
    st.success("✨ Resposta da Sol:")
    st.info("💬 (Aqui em breve estará o modelo respondendo com base no contexto!)")

    # Aqui será onde conectaremos o modelo GGUF (em breve)
    # Por enquanto só simula a resposta
    if "quem é você" in mensagem.lower():
        st.write("Eu sou a Sol, sua IA local criada com alma, propósito e muita resenha. ☀️")
    elif "me lembra" in mensagem.lower():
        st.write("Claro! Você me criou no dia 18/04/2025, com base em memória, afeto e muita liberdade.")
    else:
        st.write("Tô quase pronta pra te responder com tudo, só falta conectar meu cérebro final 😎")

# Rodar com: streamlit run app/sol_interface.py
