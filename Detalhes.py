import tkinter as tk
from tkinter import messagebox, Toplevel

# Funções para abrir as telas
def TelaDetalhes(parent):
    detalhes_window = Toplevel(parent)
    detalhes_window.title("Detalhes do Funcionário")
    detalhes_window.geometry("400x300")

    funcionario = {
        "Nome": "João Silva",
        "CPF": "12345678901",
        "Endereço": "Rua das Flores, 123",
        "Contato": "(11) 98765-4321",
        "Cargo": "Gerente"
    }

    row = 0
    for key, value in funcionario.items():
        tk.Label(detalhes_window, text=f"{key}:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        tk.Label(detalhes_window, text=value, font=("Arial", 10)).grid(row=row, column=1, sticky="w", padx=10, pady=5)
        row += 1

    tk.Button(detalhes_window, text="Fechar", command=detalhes_window.destroy).grid(row=row, column=0, columnspan=2, pady=10)

def TelaRelatorio(parent):
    relatorio_window = Toplevel(parent)
    relatorio_window.title("Relatório de Funcionários")
    relatorio_window.geometry("500x400")

    funcionarios = [
        {"Nome": "João Silva", "CPF": "12345678901", "Cargo": "Gerente"},
        {"Nome": "Maria Oliveira", "CPF": "09876543210", "Cargo": "Vendedora"},
        {"Nome": "Carlos Souza", "CPF": "56789012345", "Cargo": "Analista"}
    ]

    tk.Label(relatorio_window, text="Nome", font=("Arial", 10, "bold"), anchor="w", width=20).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(relatorio_window, text="CPF", font=("Arial", 10, "bold"), anchor="w", width=20).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(relatorio_window, text="Cargo", font=("Arial", 10, "bold"), anchor="w", width=20).grid(row=0, column=2, padx=5, pady=5)

    for i, func in enumerate(funcionarios, start=1):
        tk.Label(relatorio_window, text=func["Nome"], anchor="w").grid(row=i, column=0, padx=5, pady=2)
        tk.Label(relatorio_window, text=func["CPF"], anchor="w").grid(row=i, column=1, padx=5, pady=2)
        tk.Label(relatorio_window, text=func["Cargo"], anchor="w").grid(row=i, column=2, padx=5, pady=2)

    tk.Button(relatorio_window, text="Fechar", command=relatorio_window.destroy).grid(row=len(funcionarios) + 1, column=0, columnspan=3, pady=10)

# Janela principal
root = tk.Tk()
root.title("Sistema de Funcionários")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

btn_detalhes = tk.Button(frame, text="Abrir Detalhes", command=lambda: TelaDetalhes(root))
btn_detalhes.pack(pady=5)

btn_relatorio = tk.Button(frame, text="Abrir Relatório", command=lambda: TelaRelatorio(root))
btn_relatorio.pack(pady=5)

root.mainloop()
