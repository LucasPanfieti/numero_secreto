soma = 0

for i in range (1,4):
    nota = int(input(f"Digite a {i}º nota: "))
    soma += nota

media = soma / 3

print(f"A soma é: {soma}")
print(f"A média é: {media}")

if media < 5:
    print("Situação final: Reprovado")
elif media >= 7:
    print("Situação final: Aprovado")
else:
    print("Situação final: Recuperação")