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

    segunda_derivada = sp.diff(derivada, x) # Calcula a segunda derivada.
    print("Segunda derivada:", segunda_derivada) # Exibe a segunda derivada.
    if segunda_derivada > 0: # Verifica se o ponto é de mínimo.
        print("O ponto crítico é um mínimo.")
    elif segunda_derivada < 0: # Verifica se o ponto é de máximo.
        print("O ponto crítico é um máximo.")

    
    custo = funcao.subs(x, ponto) # Calcula o custo no ponto crítico.
    print("Custo correspondente: R$", round(float(custo), 2)) # Exibe o custo arredondado.

    
    valores_x = np.linspace(0, 40, 400) # Cria valores para o eixo X.
    valores_y = [float(funcao.subs(x, valor)) for valor in valores_x] # Calcula os valores do eixo Y.


    plt.plot(valores_x, valores_y) # Desenha a curva da função.
    plt.scatter(float(ponto), float(custo), color="red") # Marca o ponto crítico em vermelho.

    plt.title("Otimizador de Custos") # Define o título do gráfico.
    plt.xlabel("Quantidade produzida") # Nomeia o eixo X.
    plt.ylabel("Custo (R$)") # Nomeia o eixo Y.
    plt.grid() # Adiciona linhas de grade ao gráfico.
    plt.show() # Exibe o gráfico.