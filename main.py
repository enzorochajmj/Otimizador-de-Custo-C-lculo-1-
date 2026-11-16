import sympy as sp

x = sp.symbols("x")

a = float(input("Digite o valor da variável a:"))
b = float(input("Digite o valor da variável b: "))
c = float(input("Digite o valor da vaiável c: "))

funcao = a*x**2 + b*x + c
print("f(x) = ", funcao)

derivada = sp.diff(funcao, x)
print("f'(x) = ", derivada)

ponto_critico = sp.solve(derivada, x)
print("O ponto crítico é:", round([0], 2))
