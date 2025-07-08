#(ADIVINHAÇÃO DO NÚMERO SECRETO)

print("Tente adivinhar o número secreto")
y = int(input("Digite aqui: "))
x = 10

while(x != y):
    if(y > x and y <= x+5):
        print("Esta perto, tente um número menor")
    elif(y < x and y >= x-5):
        print("Esta perto, tente um número maior")
    elif(y > x):
        print("Tente um número menor")
    elif(y < x):
        print("Tente um número maior")
    y = int(input("Digite aqui: "))
    
print("Parabéns, você acertou o número secreto!!!")