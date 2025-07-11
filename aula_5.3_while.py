import random

numero_secreto = random.randint(1, 100)

tentativas = 1
chute = int(input("Adivinhe o número secreto entre 1 e 100: "))

while chute != numero_secreto:
    if chute > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")
    chute = int(input("Tente de novo: "))
    tentativas += 1
    
if tentativas == 1:
    print("Acertou de primeira! Você é brabo.")
else:
    print(f"Acertou! Com {tentativas} tentativas.")
    