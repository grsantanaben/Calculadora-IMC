import tkinter as tk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)

        if imc <= 17:
            categoria = "Magro"
        elif 18.5 <= imc <= 24.9:
            categoria = "Normal"
        elif 25 <= imc <= 25.9:
            categoria = "Sobrepeso"
        elif 30 <= imc <= 34.9:
            categoria = "Obesidade grau I"
        elif 35 <= imc <= 40:
            categoria = "Obesidade grau II"
        elif imc >= 40:
            categoria = "Obesidade grau III"
        else:
            categoria = "Fora das categorias padrão"

        print(f"IMC: {imc:.2f}, Categoria: {categoria}")
        resultado.config(text=f"Seu IMC é: {imc:.2f}\nCategoria: {categoria}")
    except ValueError:
        resultado.config(text="Por favor, insira valores válidos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

label_peso = tk.Label(janela, text="Peso:")
label_peso.pack()

entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text="Altura:")
label_altura.pack()

entry_altura = tk.Entry(janela)
entry_altura.pack()

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

# Loop principal
janela.mainloop()
