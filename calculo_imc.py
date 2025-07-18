nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em centímetros: ")) / 100
peso = float(input("Digite seu peso em kg: "))

m = peso / altura ** 2
classificacao = ""

if m < 16:
    classificacao = "Baixo peso muito grave"
elif m < 17:
    classificacao = "Baixo peso grave"
elif m < 18.50:
    classificacao = "Baixo peso"
elif m < 25:
    classificacao = "Peso normal"
elif m < 30:
    classificacao = "Sobrepeso"
elif m < 35:
    classificacao = "Obesidade grau I"
elif m < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

print(f"{nome} possui índice de massa corporal igual a {m:.2f}, sendo classificado como: {classificacao}")
