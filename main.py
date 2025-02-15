import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calcular_agua_diaria(peso, sexo):
    if sexo.lower() == 'm':
        agua_diaria = peso * 35
    elif sexo.lower() == 'f':
        agua_diaria = peso * 31
    else:
        return "Sexo não especificado corretamente. Por favor, insira 'm' para masculino ou 'f' para feminino."
    return agua_diaria

def calcular_peso_ideal(altura):
    imc_min = 18.5
    imc_max = 24.9

    peso_minimo_ideal = imc_min * (altura ** 2)
    peso_maximo_ideal = imc_max * (altura ** 2)

    return peso_minimo_ideal, peso_maximo_ideal

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def fornecer_recomendacao(imc, sexo):
    if sexo.lower() == 'm':
        if imc < 18.5:
            return "Você está abaixo do peso ideal para homens."
        elif 18.5 <= imc <= 24.9:
            return "Você está no peso ideal para homens."
        elif 25 <= imc <= 29.9:
            return "Você está acima do peso ideal para homens."
        else:
            return "Você está na faixa de obesidade para homens."
    elif sexo.lower() == 'f':
        if imc < 18.5:
            return "Você está abaixo do peso ideal para mulheres."
        elif 18.5 <= imc <= 24.9:
            return "Você está no peso ideal para mulheres."
        elif 25 <= imc <= 29.9:
            return "Você está acima do peso ideal para mulheres."
        else:
            return "Você está na faixa de obesidade para mulheres."
    else:
        return "Sexo não especificado corretamente. Por favor, insira 'm' para masculino ou 'f' para feminino."

def reset_inputs():
    peso_entry.delete(0, tk.END)
    altura_entry.delete(0, tk.END)
    sexo_var.set('m')

def calcular():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())
        sexo = sexo_var.get()

        if peso <= 0:
            messagebox.showerror("Erro", "O peso deve ser um valor positivo.")
        elif altura <= 0:
            messagebox.showerror("Erro", "A altura deve ser um valor positivo.")
        elif sexo not in ['m', 'f']:
            messagebox.showerror("Erro", "Sexo deve ser 'm' para masculino ou 'f' para feminino.")
        else:
            agua_diaria = calcular_agua_diaria(peso, sexo)
            imc_atual = calcular_imc(peso, altura)
            recomendacao = fornecer_recomendacao(imc_atual, sexo)

            messagebox.showinfo("Resultados", 
                f"Para um peso de {peso:.2f} kg, a quantidade ideal de água diária é de {agua_diaria:.2f} ml.\n\n"
                f"Com uma altura de {altura:.2f} metros, seu IMC atual é {imc_atual:.2f}.\n\n"
                f"{recomendacao}")

            # Gerar gráfico de água diária
            pesos = range(30, 151, 10)  # Exemplo de pesos de 30kg a 150kg
            aguas = [calcular_agua_diaria(p, sexo) for p in pesos]

            plt.plot(pesos, aguas, label=f'Água Diária ({sexo.upper()})')
            plt.xlabel('Peso (kg)')
            plt.ylabel('Água Diária (ml)')
            plt.title('Quantidade de Água Diária por Peso')
            plt.legend()
            plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura.")

# Interface gráfica usando Tkinter
root = tk.Tk()
root.title("Calculadora de Água Hidrofit")

# Frame para entrada de dados
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Labels e entradas
tk.Label(frame, text="Digite seu peso em kg:").grid(row=0, column=0, padx=5, pady=5)
peso_entry = tk.Entry(frame)
peso_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Digite sua altura em metros:").grid(row=1, column=0, padx=5, pady=5)
altura_entry = tk.Entry(frame)
altura_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Selecione seu sexo:").grid(row=2, column=0, padx=5, pady=5)
sexo_var = tk.StringVar(value='m')
sexo_select = tk.OptionMenu(frame, sexo_var, 'm', 'f')
sexo_select.grid(row=2, column=1, padx=5, pady=5)

# Botões
tk.Button(root, text="Calcular", command=calcular).pack(pady=10)
tk.Button(root, text="Reiniciar", command=reset_inputs).pack()

root.mainloop()




