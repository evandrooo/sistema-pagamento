import streamlit as st

# ==== Dados de login simples (Exemplo - em produção use um banco de dados) ====
USERS = {
    "admin": "1234",
    "usuario": "senha"
}

# ==== Função de login ====
def login():
    st.title("Login do Sistema de Pagamentos")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.success(f"Bem-vindo, {username}!")
        else:
            st.error("Usuário ou senha incorretos.")

# ==== Função para registrar pagamentos ====
def payment_system():
    st.title("Sistema de Pagamento")

    # Inicializar lista de pagamentos
    if "payments" not in st.session_state:
        st.session_state.payments = []

    with st.form("payment_form"):
        cliente = st.text_input("Nome do Cliente")
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
        forma = st.selectbox("Forma de Pagamento", ["Dinheiro", "Pix", "Cartão de Crédito", "Cartão de Débito"])
        enviar = st.form_submit_button("Registrar Pagamento")

        if enviar and cliente and valor > 0:
            st.session_state.payments.append({
                "Cliente": cliente,
                "Valor": f"R$ {valor:.2f}",
                "Forma": forma
            })
            st.success("Pagamento registrado com sucesso!")

    # Exibir pagamentos registrados
    st.subheader("Pagamentos Registrados")
    for idx, pagamento in enumerate(st.session_state.payments):
        st.write(f"{idx+1}. Cliente: {pagamento['Cliente']} | Valor: {pagamento['Valor']} | Forma: {pagamento['Forma']}")

    # Botão de logout
    if st.button("Sair"):
        st.session_state.logged_in = False

# ==== Controle de Acesso ====
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    payment_system()
