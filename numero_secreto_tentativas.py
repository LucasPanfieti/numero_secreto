#(ADIVINHAÇÃO DO NÚMERO SECRETO - COM TENTATIVAS)

n = 10 #numero_secreto
t = 5 #tentativas
print("Tente adivinhar o número secreto (você tem",t,"tentativas)")

while(t > 0):
    y = int(input("Digite aqui: ")) #palpite
    t -= 1
    if(y == n):
        print("Parabéns, você acertou o número secreto!!!")
        break
    elif(t == 0):
        print("Você perdeu, acabaram suas tentativas :(")
        break
    elif(y > n and y <= n+5):
        print("Esta perto, tente um número menor")
    elif(y < n and y >= n-5):
        print("Esta perto, tente um número maior")
    elif(y > n):
        print("Tente um número menor")
    else:
        print("Tente um número maior")
    print("Tentativas restantes:",t)