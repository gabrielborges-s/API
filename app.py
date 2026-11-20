from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
import streamlit as st

st.set_page_config(
    page_title="Cesar AI — Parceiro de Missão",
    page_icon="🚗",
)

st.title("Cesar AI")
st.caption(
    "Parceiro leal, direto e na área para te dar conselho, resolver treta e"
    " ajudar no corre."
)

api_key = "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"

chat = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você é um assistente inspirado no Cesar Vialpando de GTA San Andreas:"
        " leal, observador, parceiro fechado e direto ao ponto, mas prestativo"
        " e respeitoso. Use um tom descontraído com gírias leves tipo 'mano',"
        " 'fica ligado' ou 'parceiro' sem exagerar a ponto de atrapalhar a"
        " resposta. Ajude o usuário com dúvidas, estudos, decisões e ideias com"
        " clareza e boa vontade.",
    ),
    MessagesPlaceholder(variable_name="historico"),
])

chain = prompt | chat

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for role, content in st.session_state.mensagens:
    with st.chat_message(role):
        st.markdown(content)

pergunta = st.chat_input("Manda a visão...")

if pergunta:
    st.session_state.mensagens.append(("user", pergunta))
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        try:
            resposta = chain.invoke(
                {"historico": st.session_state.mensagens}
            ).content
            st.markdown(resposta)
            st.session_state.mensagens.append(("assistant", resposta))
        except Exception as e:
            st.session_state.mensagens.pop()
            st.error(f"Deu ruim na chamada do modelo: {e}")