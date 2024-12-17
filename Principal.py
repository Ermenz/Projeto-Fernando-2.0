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
    search_window.geometry("650x400")

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

# Funções de Alterar e Excluir
def alterar():
    messagebox.showinfo("Alterar", "Botão Alterar clicado!")

def excluir():
    messagebox.showinfo("Excluir", "Botão Excluir clicado!")

def verificarCaminhoes():
    caminhoes = Toplevel(root)
    caminhoes.title("Caminhões")
    caminhoes.geometry("650x400")

    resultados_caminhoes = [
        {"EntradaESaida" : "11.50-15.30", "Nome" : "Scannia 113", "Manuntencao" : "Sim"},
        {"EntradaESaida" : "6.30-13.00", "Nome" : "VUC", "Manuntencao" : "Não"}
    ]

    tk.Label(caminhoes, text="Entrada_Saída", width=15, anchor="w", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=2)
    tk.Label(caminhoes, text="Caminhão", width=15, anchor="w", font=("Arial", 10, "bold")).grid(row=1, column=1, padx=5, pady=2)
    tk.Label(caminhoes, text="Manuntenção", width=15, anchor="w", font=("Arial", 10, "bold")).grid(row=1, column=2, padx=5, pady=2)
    
    # Exibir resultados
    for i, resultados_caminhoes in enumerate (resultados_caminhoes, start=2):
        tk.Label(caminhoes, text=resultados_caminhoes["EntradaESaida"], anchor="w").grid(row=i, column=0, padx=5, pady=2)
        tk.Label(caminhoes, text=resultados_caminhoes["Nome"], anchor="w").grid(row=i, column=1, padx=5, pady=2)
        tk.Label(caminhoes, text=resultados_caminhoes["Manuntencao"], anchor="w").grid(row=i, column=2, padx=5, pady=2)


   

def clientes():
    clientes = Toplevel(root)
    clientes.title("Clientes")
    clientes.geometry("650x400")

    resultados_clientes = [
        {
            "Nome": "Maira Santos",
            "CPF": "14155532514",
            "Endereco": "Rua Bahia, Pituba, Salvador"
        },

        {
            "Nome" : "Carlos Santana",
            "CPF" : "58969742457",
            "Endereco" : "Av Dom João VI, Brotas, Salvador"
        } 
    ]

    tk.Label(clientes, text="Nome", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)    
    tk.Label(clientes, text="CPF", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)    
    tk.Label(clientes, text="Endereço", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)    

    
    for i, resultados_clientes in enumerate(resultados_clientes, start=1):
        tk.Label(clientes, text=resultados_clientes["Nome"], anchor="w").grid(row=i, column=0, padx=5, pady=2)
        tk.Label(clientes, text=resultados_clientes["CPF"], anchor="w").grid(row=i, column=1, padx=5, pady=2)
        tk.Label(clientes, text=resultados_clientes["Endereco"], anchor="w").grid(row=i, column=2, padx=5, pady=2)


def sensores():
    sensores = Toplevel(root)
    sensores.title("Sensores")
    sensores.geometry("650x400")

    resultados_sensores = [
        {
            "Tipo":"Temperatura" ,
            "Ha":"Presente",
            "Preco":"R$25,00"
        } ,
        {
            "Tipo":"Luminosidade",
            "Ha":"Em falta",
            "Preco":"R$30,00",
        }
    ]

    tk.Label(sensores, text="Tipo", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)    
    tk.Label(sensores, text="Presente/Em falta", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)    
    tk.Label(sensores, text="Preço", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)    

    for i, resultados_sensores in enumerate(resultados_sensores, start= 1):
        tk.Label(sensores, text=resultados_sensores["Tipo"], anchor="w").grid(row=i, column=0, padx=5, pady=2)
        tk.Label(sensores, text=resultados_sensores["Ha"], anchor="w").grid(row=i, column=1, padx=5, pady=2)
        tk.Label(sensores, text=resultados_sensores["Preco"], anchor="w").grid(row=i, column=2, padx=5, pady=2)


# Janela Principal
root = tk.Tk()
root.title("Cadastro de Funcionários ou de fornecedores")
root.geometry("650x400")

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

tk.Label(frame, text="Fornecedor:").grid(row=6, column=0, sticky="w", pady=5)
entry_fornecedor = tk.Entry(frame, width=40)
entry_fornecedor.grid(row=6, column=1, pady=5)

tk.Label(frame, text="Produto:").grid(row=7, column=0, sticky="w", pady=5)
entry_produto = tk.Entry(frame, width=40)
entry_produto.grid(row=7, column=1, pady=5)

button_frame = tk.Frame(root, pady=10)
button_frame.pack()

btn_inserir = tk.Button(button_frame, text="Inserir", width=10, command=inserir)
btn_inserir.grid(row=0, column=0, padx=5)

btn_pesquisar = tk.Button(button_frame, text="Pesquisar", width=10, command=pesquisar)
btn_pesquisar.grid(row=0, column=1, padx=5)

btn_alterar = tk.Button(button_frame, text="Alterar", width=10, command=alterar)
btn_alterar.grid(row=0, column=2, padx=5)

btn_excluir = tk.Button(button_frame, text="Excluir", width=10, command=excluir)
btn_excluir.grid(row=0, column=3, padx=5)

btn_VerificarCaminhoes = tk.Button(button_frame, text="Caminhões", width=10, command=verificarCaminhoes)
btn_VerificarCaminhoes.grid(row=0, column=4, padx=5)

btn_clientes = tk.Button(button_frame, text="Clientes", width=10, command=clientes)
btn_clientes.grid(row=1, column=1, pady=5)

btn_sensores = tk.Button(button_frame, text="Sensores", width=10, command=sensores)
btn_sensores.grid(row=2, column=1, pady=5)



root.mainloop()
