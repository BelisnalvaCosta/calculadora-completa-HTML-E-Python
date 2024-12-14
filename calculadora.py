import tkinter as tk
from tkinter import messagebox
from math import factorial
from sympy import isprime

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def power(a, b):
    return a ** b

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def perform_operation():
    try:
        operation = operation_var.get()
        num1 = float(entry_num1.get())
        
        if operation in ["Soma", "Subtração", "Multiplicação", "Divisão", "Potência"]:
            num2 = float(entry_num2.get())
            if operation == "Soma":
                result = add(num1, num2)
            elif operation == "Subtração":
                result = subtract(num1, num2)
            elif operation == "Multiplicação":
                result = multiply(num1, num2)
            elif operation == "Divisão":
                result = divide(num1, num2)
            elif operation == "Potência":
                result = power(num1, num2)

        elif operation == "Fatorial":
            if num1 < 0 or not num1.is_integer():
                result = "Erro: Fatorial é definido apenas para inteiros não-negativos."
            else:
                result = factorial(int(num1))

        elif operation == "Verificar se é Par":
            result = "Par" if is_even(num1) else "Ímpar"

        elif operation == "Verificar se é Primo":
            result = "Primo" if isprime(int(num1)) else "Não Primo"

        else:
            result = "Operação não reconhecida."

        result_label.config(text=f"Resultado: {result}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora Interativa")
root.geometry("400x400")
root.config(bg="#87CEEB")

title_label = tk.Label(root, text="Calculadora Completa", font=("Arial", 16, "bold"), bg="#87CEEB", fg="white")
title_label.pack(pady=10)

# Entrada de números
entry_num1 = tk.Entry(root, font=("Arial", 14), width=10)
entry_num1.pack(pady=5)

entry_num2 = tk.Entry(root, font=("Arial", 14), width=10)
entry_num2.pack(pady=5)

# Menu de operações
operation_var = tk.StringVar(value="Soma")
operations_menu = tk.OptionMenu(root, operation_var, "Soma", "Subtração", "Multiplicação", "Divisão", "Potência", "Fatorial", "Verificar se é Par", "Verificar se é Primo")
operations_menu.pack(pady=10)

# Botão de cálculo
calculate_button = tk.Button(root, text="Calcular", font=("Arial", 14, "bold"), bg="#4682B4", fg="white", command=perform_operation)
calculate_button.pack(pady=10)

# Rótulo de resultado
result_label = tk.Label(root, text="Resultado: ", font=("Arial", 14), bg="#87CEEB", fg="white")
result_label.pack(pady=20)

root.mainloop()