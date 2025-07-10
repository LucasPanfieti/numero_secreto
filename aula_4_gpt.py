try:
    nota = float(input("Digite a nota (de 0 a 10): "))
    nota = round(nota, 2)  # Arredonda a nota para 2 casas
    situacao = None

    if 0 <= nota <= 10:
        if nota < 5:
            situacao = "Reprovado"
        elif nota < 7:
            situacao = "Recuperação"
        else:
            situacao = "Aprovado"
    else:
        situacao = False

    if situacao == False:
        print("A nota não está certa!")
    else:
        print(f"Nota: {nota:.2f} - {situacao}")

except ValueError:
    print("Você digitou um valor inválido! Digite um número entre 0 e 10.")