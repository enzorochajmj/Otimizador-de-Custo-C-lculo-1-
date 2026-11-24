import sympy as sp #biblioteca de derivação 
import numpy as np #biblioteca de trabalho com números, gera sequências de quantidades
import matplotlib.pyplot as plt #biblioteca com ferramentas de criação de gráficos

x = sp.symbols("x") #definir "x" como uma variável 

a = float(input("Digite o valor da variável a:")) #pedido do valor das variáveis
b = float(input("Digite o valor da variável b: ")) #pedido do valor das variáveis
c = float(input("Digite o valor da variável c: ")) #pedido do valor das variáveis 

funcao = a*x**2 + b*x + c #função quadrática montada
print("f(x) = ", funcao) #imprime a função montada no terminal

derivada = sp.diff(funcao, x) #pedido para sympy derivar função 
print("f'(x) = ", derivada) #impressao da derivada 

ponto_critico = sp.solve(derivada, x) #resolve a equação e iguala a 0, ex: 2x -40 = 0. resultado em lista, ex [20, 0]
if len(ponto_critico) == 0: #ler a lista e caso não tenha nenhum número, não tem ponto crítico
    print("Não existem pontos críticos.") #imprime se for o caso
else:
    ponto = ponto_critico[0] #caso tenha número, é impresso o primeiro da lista que começa no 0, ex: ponto 20.0
    print("O ponto crítico é:", round(float(ponto), 2)) #imprime o ponto crítico em 2 casas decimais

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