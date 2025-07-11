soma = 0
par_ou_impar = None

for i in range(1,4):
    n = int(input(f"Digite o {i}º número:"))
    soma += n
    
print(f"Soma total: {soma}")
    
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")
