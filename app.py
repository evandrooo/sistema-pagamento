import streamlit as st
from datetime import datetime, date

# ==== Usuários do sistema ====
USERS = {
    "admin": "1234",
    "usuario": "senha"
}

# ==== Login ====
def login():
    st.title("Login do Sistema de Pagamentos")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Bem-vindo, {username}!")
        else:
            st.error("Usuário ou senha incorretos.")

# ==== Sistema de pagamento ====
def payment_system():
    st.title("Sistema de Pagamento Profissional")

    # Inicializa lista de pagamentos
    if "payments" not in st.session_state:
        st.session_state.payments = []

    with st.form("form_pagamento"):
        cliente = st.text_input("Nome do Cliente")
        produto = st.text_input("Produto Pago")
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
        forma = st.selectbox("Forma de Pagamento", ["Dinheiro", "Pix", "Cartão de Crédito", "Cartão de Débito"])
        vencimento = st.date_input("Data de Vencimento", min_value=date.today())
        data_pagamento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        enviar = st.form_submit_button("Registrar Pagamento")

        if enviar and cliente and produto and valor > 0:
            st.session_state.payments.append({
                "Cliente": cliente,
                "Produto": produto,
                "Valor": f"R$ {valor:.2f}",
                "Forma": forma,
                "Registrado por": st.session_state["username"],
                "Data de Pagamento": data_pagamento,
                "Data de Vencimento": vencimento.strftime("%d/%m/%Y")
            })
            st.success("Pagamento registrado com sucesso!")

    # Lista de pagamentos
    st.subheader("Pagamentos Registrados")
    for i, p in enumerate(st.session_state.payments):
        st.markdown(f"""
        **{i+1}. Cliente:** {p['Cliente']}  
        **Produto:** {p['Produto']}  
        **Valor:** {p['Valor']}  
        **Forma de Pagamento:** {p['Forma']}  
        **Data de Pagamento:** {p['Data de Pagamento']}  
        **Data de Vencimento:** {p['Data de Vencimento']}  
        **Registrado por:** {p['Registrado por']}  
        ---
        """)

    # Logout
    if st.button("Sair"):
        st.session_state.logged_in = False
        st.session_state.username = ""

# ==== Controle de login ====
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if not st.session_state.logged_in:
    login()
else:
    payment_system()
