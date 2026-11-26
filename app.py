from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
import streamlit as st

st.set_page_config(
    page_title="Cesar AI — Parceiro de Missão",
    page_icon="🚗",
)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("data:image/webp;base64,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");
        background-size: cover;
        background-position: center 1%;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    [data-testid="stChatMessage"] {
        background-color: rgba(17, 19, 24, 0.78);
        border-radius: 12px;
        padding: 0.5rem 0.75rem;
    }

    [data-testid="stChatInput"] {
        background-color: rgba(17, 19, 24, 0.85);
        border-radius: 12px;
    }

    .stApp h1,
    .stApp .stCaption,
    .stApp .stCaption p,
    .stApp [data-testid="stMarkdownContainer"] p {
        color: #ffffff;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 0.75);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
