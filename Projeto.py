#Turma: 88433
#Componentes da equipe: Erick Menezes, João Miranda, Uillian Anderson, Marcos André.

import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from datetime import datetime

# Validação de CPF
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Validação de Data
def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Função para inserir um funcionário
def inserir():
    nome = entry_nome.get().strip()
    cpf = entry_cpf.get().strip()
    data_nascimento = entry_data_nascimento.get().strip()

    if not nome:
        messagebox.showwarning("Campo Obrigatório", "O campo Nome é obrigatório.")
        entry_nome.focus()
        return
    if not cpf:
        messagebox.showwarning("Campo Obrigatório", "O campo CPF é obrigatório.")
        entry_cpf.focus()
        return
    if not validar_cpf(cpf):
        messagebox.showwarning("CPF Inválido", "Por favor, insira um CPF válido (11 dígitos).")
        entry_cpf.focus()
        return
    if data_nascimento and not validar_data(data_nascimento):
        messagebox.showwarning("Data Inválida", "Por favor, insira uma data válida no formato dd/mm/aaaa.")
        entry_data_nascimento.focus()
        return

    messagebox.showinfo("Inserir", "Funcionário inserido com sucesso!")

# Nova tela para exibir os resultados da pesquisa
def pesquisar():
    # Janela de Pesquisa
    search_window = Toplevel(root)
    search_window.title("Resultados da Pesquisa")
    search_window.geometry("400x300")

    # Dados simulados
    resultados = [
        {"Nome": "João Silva", "CPF": "12345678901", "Cargo": "Gerente"},
        {"Nome": "Maria Oliveira", "CPF": "09876543210", "Cargo": "Vendedora"}
    ]

    # Títulos das colunas
    tk.Label(search_window, text="Nome", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(search_window, text="CPF", width=15, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(search_window, text="Cargo", width=15, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)

    # Exibir resultados
    for i, resultado in enumerate(resultados, start=1):
        tk.Label(search_window, text=resultado["Nome"], anchor="w").grid(row=i, column=0, padx=5, pady=2)
        tk.Label(search_window, text=resultado["CPF"], anchor="w").grid(row=i, column=1, padx=5, pady=2)
        tk.Label(search_window, text=resultado["Cargo"], anchor="w").grid(row=i, column=2, padx=5, pady=2)

    # Botão para fechar a janela de pesquisa
    btn_fechar = tk.Button(search_window, text="Fechar", width=10, command=search_window.destroy)
    btn_fechar.grid(row=i + 1, column=0, columnspan=3, pady=10)

# Função de Alterar
def abrir_tela_alterar():
    alterar_window = Toplevel(root)
    alterar_window.title("Alterar Funcionário")
    alterar_window.geometry("400x300")

    # Labels e campos de entrada para a alteração
    tk.Label(alterar_window, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
    entry_nome_alterar = tk.Entry(alterar_window, width=40)
    entry_nome_alterar.grid(row=0, column=1, pady=5)

    tk.Label(alterar_window, text="CPF:").grid(row=1, column=0, sticky="w", pady=5)
    entry_cpf_alterar = tk.Entry(alterar_window, width=40)
    entry_cpf_alterar.grid(row=1, column=1, pady=5)

    tk.Label(alterar_window, text="Cargo:").grid(row=2, column=0, sticky="w", pady=5)
    entry_cargo_alterar = tk.Entry(alterar_window, width=40)
    entry_cargo_alterar.grid(row=2, column=1, pady=5)

    def confirmar_alteracao():
        messagebox.showinfo("Alterar", "Alteração realizada com sucesso!")

    btn_confirmar = tk.Button(alterar_window, text="Confirmar Alteração", width=20, command=confirmar_alteracao)
    btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)

# Função de Excluir
def abrir_tela_excluir():
    excluir_window = Toplevel(root)
    excluir_window.title("Excluir Funcionário")
    excluir_window.geometry("400x200")

    # Campo para inserir CPF para exclusão
    tk.Label(excluir_window, text="CPF para Exclusão:").grid(row=0, column=0, sticky="w", pady=5)
    entry_cpf_excluir = tk.Entry(excluir_window, width=40)
    entry_cpf_excluir.grid(row=0, column=1, pady=5)

    def confirmar_exclusao():
        messagebox.showinfo("Excluir", "Funcionário excluído com sucesso!")

    btn_confirmar = tk.Button(excluir_window, text="Confirmar Exclusão", width=20, command=confirmar_exclusao)
    btn_confirmar.grid(row=1, column=0, columnspan=2, pady=10)

# Janela Principal
root = tk.Tk()
root.title("Cadastro de Funcionários")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame, width=40)
entry_nome.grid(row=0, column=1, pady=5)

tk.Label(frame, text="CPF:").grid(row=1, column=0, sticky="w", pady=5)
entry_cpf = tk.Entry(frame, width=40)
entry_cpf.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Endereço:").grid(row=2, column=0, sticky="w", pady=5)
entry_endereco = tk.Entry(frame, width=40)
entry_endereco.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Contato:").grid(row=3, column=0, sticky="w", pady=5)
entry_contato = tk.Entry(frame, width=40)
entry_contato.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Cargo:").grid(row=4, column=0, sticky="w", pady=5)
entry_cargo = tk.Entry(frame, width=40)
entry_cargo.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Data de Nascimento (dd/mm/aaaa):").grid(row=5, column=0, sticky="w", pady=5)
entry_data_nascimento = tk.Entry(frame, width=40)
entry_data_nascimento.grid(row=5, column=1, pady=5)

button_frame = tk.Frame(root, pady=10)
button_frame.pack()

btn_inserir = tk.Button(button_frame, text="Inserir", width=10, command=inserir)
btn_inserir.grid(row=0, column=0, padx=5)

btn_pesquisar = tk.Button(button_frame, text="Pesquisar", width=10, command=pesquisar)
btn_pesquisar.grid(row=0, column=1, padx=5)

btn_alterar = tk.Button(button_frame, text="Alterar", width=10, command=abrir_tela_alterar)
btn_alterar.grid(row=0, column=2, padx=5)

btn_excluir = tk.Button(button_frame, text="Excluir", width=10, command=abrir_tela_excluir)
btn_excluir.grid(row=0, column=3, padx=5)

root.mainloop()
