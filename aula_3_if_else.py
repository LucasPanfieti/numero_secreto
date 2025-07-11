numero1 = 15
numero2 = 4

soma = numero1 + numero2
divisao_real = numero1 / numero2
potencia = numero1 ** numero2
resto_da_divisao = numero1 % numero2

n1_maior_que_n2 = numero1 > numero2

print(f"Soma: {soma}")
print(f"Divisão real: {divisao_real}")
print(f"Potência: {potencia}")
print(f"Resto da divisão: {resto_da_divisao}")

if n1_maior_que_n2:
    print("numero1 é maior que numero2")
else:
    print("numero1 não é maior que numero2")
    
pode_prosseguir = numero1 > numero2 and resto_da_divisao != 0

print(pode_prosseguir)
    