import tkinter as tk
from tkinter import messagebox

def login(entry_username, entry_password):
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Campos Obrigatórios", "Usuário e Senha são obrigatórios!")
    else:
        messagebox.showinfo("Login", f"Bem-vindo, {username}!")

def esqueci_senha():
    messagebox.showinfo("Esqueci a Senha", "A funcionalidade de recuperação de senha foi acionada!")

def tela_login():
    root = tk.Tk()
    root.title("Login de Usuário")
    root.geometry("300x200")

    tk.Label(root, text="Usuário:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_username = tk.Entry(root, width=30)
    entry_username.grid(row=0, column=1, pady=5)

    tk.Label(root, text="Senha:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_password = tk.Entry(root, width=30, show="*")
    entry_password.grid(row=1, column=1, pady=5)

    btn_login = tk.Button(root, text="Entrar", width=10, 
                          command=lambda: login(entry_username, entry_password))
    btn_login.grid(row=2, column=0, padx=5, pady=10)

    btn_esqueci = tk.Button(root, text="Esqueci a Senha", width=15, command=esqueci_senha)
    btn_esqueci.grid(row=2, column=1, padx=5, pady=10)

    btn_sair = tk.Button(root, text="Sair", width=10, command=root.destroy)
    btn_sair.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

# Chamando a tela de login
tela_login()
