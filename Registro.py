import tkinter as tk
from tkinter import messagebox

def registrar(entry_reg_username, entry_reg_password, entry_confirm_password):
    username = entry_reg_username.get().strip()
    password = entry_reg_password.get().strip()
    confirm_password = entry_confirm_password.get().strip()

    if not username or not password or not confirm_password:
        messagebox.showwarning("Campos Obrigatórios", "Todos os campos são obrigatórios!")
    elif password != confirm_password:
        messagebox.showerror("Erro", "As senhas não coincidem!")
    else:
        messagebox.showinfo("Registro", f"Usuário '{username}' registrado com sucesso!")

def tela_registro():
    root = tk.Tk()
    root.title("Registro de Usuário")
    root.geometry("350x250")

    tk.Label(root, text="Usuário:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_reg_username = tk.Entry(root, width=30)
    entry_reg_username.grid(row=0, column=1, pady=5)

    tk.Label(root, text="Senha:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_reg_password = tk.Entry(root, width=30, show="*")
    entry_reg_password.grid(row=1, column=1, pady=5)

    tk.Label(root, text="Confirmar Senha:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_confirm_password = tk.Entry(root, width=30, show="*")
    entry_confirm_password.grid(row=2, column=1, pady=5)

    btn_registrar = tk.Button(root, text="Registrar", width=10, 
                               command=lambda: registrar(entry_reg_username, entry_reg_password, entry_confirm_password))
    btn_registrar.grid(row=3, column=0, padx=5, pady=10)

    btn_esqueci = tk.Button(root, text="Esqueci a Senha", width=15, command=lambda: print("Função de esqueci a senha"))
    btn_esqueci.grid(row=3, column=1, padx=5, pady=10)

    btn_sair = tk.Button(root, text="Sair", width=10, command=root.destroy)
    btn_sair.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

# Chamando a tela de registro
tela_registro()
