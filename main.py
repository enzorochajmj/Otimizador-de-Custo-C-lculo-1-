import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols("x")

a = float(input("Digite o valor da variável a:"))
b = float(input("Digite o valor da variável b: "))
c = float(input("Digite o valor da variável c: "))

funcao = a*x**2 + b*x + c
print("f(x) = ", funcao)

derivada = sp.diff(funcao, x)
print("f'(x) = ", derivada)

ponto_critico = sp.solve(derivada, x)
if len(ponto_critico) == 0:
    print("Não existem pontos críticos.")
else:
    ponto = ponto_critico[0]
    print("O ponto crítico é:", round(float(ponto), 2))

    segunda_derivada = sp.diff(derivada, x)
    print("Segunda derivada:", segunda_derivada)
    if segunda_derivada > 0:
        print("O ponto crítico é um mínimo.")
    elif segunda_derivada < 0:
        print("O ponto crítico é um máximo.")

    
    custo = funcao.subs(x, ponto)
    print("Custo correspondente: R$", round(float(custo), 2))

    
    valores_x = np.linspace(0, 40, 400)
    valores_y = [float(funcao.subs(x, valor)) for valor in valores_x]

    plt.plot(valores_x, valores_y)
    plt.scatter(float(ponto), float(custo), color="red")

    plt.title("Otimizador de Custos")
    plt.xlabel("Quantidade produzida")
    plt.ylabel("Custo (R$)")
    plt.grid()
    plt.show()