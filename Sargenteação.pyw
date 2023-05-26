import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
from cadastro import cadastrar_militar

login_window = None  # Variável global para a janela de login
login_status_label = None  # Variável global para o rótulo de status de login

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def funcao_cadastro():
    # Lógica para ação de cadastro
    print("Função de cadastrar executada")

def fazer_login(username_entry, password_entry):
    global login_status_label  # Declarar a variável como global

    usuario = username_entry.get()
    senha = password_entry.get()

    # Verificar usuário e senha
    if usuario == "admin" and senha == "senha123":
        login_window.destroy()
        criar_janela_principal()
        abrir_janela_banco_dados()
    else:
        login_status_label.config(text="Usuário ou senha incorretos")

def confirmar_fechamento():
    resposta = messagebox.askyesno("Confirmação", "Deseja sair do programa?")
    if resposta:
        janela_principal.destroy()

def confirmar_fechamento():
    resposta = messagebox.askyesno("Confirmação", "Deseja sair do programa?")
    if resposta:
        janela_principal.destroy()
    

def criar_janela_principal():
    global janela_principal

    janela_principal = tk.Tk()
    janela_principal.title("Programa de Cadastro Militar")
    janela_principal.geometry("800x600")  # Definindo o tamanho inicial da janela principal

    # Função para redimensionar a imagem de fundo
    def redimensionar_imagem(event):
        # Obtém as dimensões da janela principal
        largura = event.width
        altura = event.height

        # Redimensiona a imagem de acordo com as novas dimensões
        imagem_redimensionada = imagem_principal.resize((largura, altura), Image.ANTIALIAS)
        imagem_fundo_principal = ImageTk.PhotoImage(imagem_redimensionada)

        # Atualiza a imagem de fundo na label
        label_imagem_fundo_principal.configure(image=imagem_fundo_principal)
        label_imagem_fundo_principal.image = imagem_fundo_principal

    # Carregar imagem de fundo da janela principal
    imagem_principal = Image.open("imagem.jpg")
    imagem_fundo_principal = ImageTk.PhotoImage(imagem_principal)

    # Exibir imagem de fundo da janela principal
    label_imagem_fundo_principal = tk.Label(janela_principal, image=imagem_fundo_principal)
    label_imagem_fundo_principal.place(x=0, y=0, relwidth=1, relheight=1)
    label_imagem_fundo_principal.bind("<Configure>", redimensionar_imagem)

    # Exibir imagem de fundo da janela principal
    label_imagem_fundo_principal = tk.Label(janela_principal, image=imagem_fundo_principal)
    label_imagem_fundo_principal.place(x=0, y=0, relwidth=1, relheight=1)
    label_imagem_fundo_principal.bind("<Configure>", redimensionar_imagem)

    # Botão para abrir a janela de Banco de Dados
    botao_banco_dados = tk.Button(janela_principal, text="Banco de Dados", command=abrir_janela_banco_dados)
    botao_banco_dados.place(relx=0, rely=0, anchor="nw")

    centralizar_janela(janela_principal)

    # Definir função de confirmação de fechamento ao fechar a janela principal
    janela_principal.protocol("WM_DELETE_WINDOW", confirmar_fechamento)

    janela_principal.mainloop()

def abrir_janela_banco_dados():
    janela_banco_dados = tk.Toplevel(janela_principal)
    janela_banco_dados.title("Banco de Dados")
    janela_banco_dados.geometry("400x300")  # Definindo o tamanho da janela de banco de dados
    janela_banco_dados.resizable(False, False)  # Desabilitar redimensionamento da janela
    centralizar_janela(janela_banco_dados)

    # Carregar imagem de fundo da janela de banco de dados
    imagem_banco_dados = Image.open("imagem2.png")
    imagem_banco_dados = imagem_banco_dados.resize((400, 300), Image.ANTIALIAS)
    imagem_fundo_banco_dados = ImageTk.PhotoImage(imagem_banco_dados)

    # Exibir imagem de fundo da janela de banco de dados
    label_imagem_fundo_banco_dados = tk.Label(janela_banco_dados, image=imagem_fundo_banco_dados)
    label_imagem_fundo_banco_dados.place(x=0, y=0, relwidth=1, relheight=1)

    # Botão de busca
    botao_busca = tk.Button(janela_banco_dados, text="Buscar Militar", command=funcao_busca)
    botao_busca.place(relx=0.5, rely=0.5, anchor="center")

    # Botão de cadastro
    botao_cadastro = tk.Button(janela_banco_dados, text="Cadastrar Militar", command=funcao_cadastro)
    botao_cadastro.place(relx=0.5, rely=0.6, anchor="center")


    janela_banco_dados.mainloop()

def funcao_busca():
    # Lógica para ação de busca
    print("Função de busca executada") 
    
def funcao_cadastro():
    # Lógica para ação de cadastro
    print("Função de cadastrar executada")

    # Chamar a função de cadastro do arquivo separado
    cadastrar_militar(nome, idade, posto_grad, especialidade)       

def criar_janela_login():
    global login_window

    def validar_login(event=None):
        fazer_login(username_entry, password_entry)

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("200x100")  # Definindo o tamanho da janela de login

    # Impedir o redimensionamento da janela
    login_window.resizable(False, False)

    username_label = tk.Label(login_window, text="Usuário:")
    username_label.pack()

    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text="Senha:")
    password_label.pack()

    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    login_button = tk.Button(login_window, text="Entrar", command=lambda: fazer_login(username_entry, password_entry))
    login_button.pack()

    login_status_label = tk.Label(login_window, text="")
    login_status_label.pack()

    def atualizar_imagem_titulo():
        imagem_titulo = Image.open("imglogin.png")
        imagem_titulo = imagem_titulo.resize((200, 50), Image.ANTIALIAS)
        imagem_titulo = ImageTk.PhotoImage(imagem_titulo)

        login_window.iconphoto(False, imagem_titulo)

    # Carregar imagem do título da janela de login
    imagem_titulo = Image.open("imglogin.png")
    imagem_titulo = imagem_titulo.resize((200, 50), Image.ANTIALIAS)
    imagem_titulo = ImageTk.PhotoImage(imagem_titulo)

    login_window.iconphoto(False, imagem_titulo)

    centralizar_janela(login_window)

    login_window.bind("<Return>", validar_login)    

    login_window.mainloop()

criar_janela_login()