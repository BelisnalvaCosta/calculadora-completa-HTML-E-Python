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

def append_to_entry(value):
    entry_display.insert(tk.END, value)

def clear_entry():
    entry_display.delete(0, tk.END)

def backspace():
    current_text = entry_display.get()
    entry_display.delete(len(current_text) - 1, tk.END)

def calculate_result():
    try:
        expression = entry_display.get()
        if "!" in expression:
            number = int(expression.replace("!", ""))
            result = factorial(number)
        elif "isprime" in expression:
            number = int(expression.replace("isprime", ""))
            result = "Primo" if isprime(number) else "Não Primo"
        else:
            result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora Avançada")
root.geometry("350x500")
root.config(bg="#1E1E1E")

# Display
entry_display = tk.Entry(root, font=("Arial", 24), bg="#EEE", fg="#333", justify="right")
entry_display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10, padx=10)

# Botões
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("(", 5, 0), (")", 5, 1), (".", 5, 2), ("^", 5, 3),
    ("isprime", 6, 0), ("!", 6, 1), ("<-", 6, 2), ("%", 6, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#87CEEB", fg="white", command=calculate_result)
    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#FF6347", fg="white", command=clear_entry)
    elif text == "<-":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#FF6347", fg="white", command=backspace)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#D3D3D3", fg="#000",
                        command=lambda t=text: append_to_entry(t if t != "^" else "**"))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Ajustar tamanho automático das células
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()

