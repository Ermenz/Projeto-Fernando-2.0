import tkinter as tk
from tkinter import messagebox

def enviar_mensagem(entry_mensagem):
    mensagem = entry_mensagem.get("1.0", "end-1c").strip()  # Pega o texto da caixa de mensagem

    if not mensagem:
        messagebox.showwarning("Campo Obrigatório", "A mensagem não pode estar vazia!")
    else:
        # Aqui você pode adicionar o código para enviar a mensagem ao suporte
        messagebox.showinfo("Mensagem Enviada", "Sua mensagem foi enviada com sucesso!")

def tela_contato():
    root = tk.Tk()
    root.title("Contato com o Suporte")
    root.geometry("400x300")

    tk.Label(root, text="Escreva sua mensagem para o Suporte:").pack(padx=10, pady=10)

    entry_mensagem = tk.Text(root, width=40, height=8)
    entry_mensagem.pack(padx=10, pady=10)

    btn_enviar = tk.Button(root, text="Enviar Mensagem", width=20, 
                           command=lambda: enviar_mensagem(entry_mensagem))
    btn_enviar.pack(pady=10)

    btn_sair = tk.Button(root, text="Sair", width=10, command=root.destroy)
    btn_sair.pack(pady=10)

    root.mainloop()

# Chamando a tela de contato
tela_contato()
