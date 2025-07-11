opcao = None

while opcao != 5:
    print("\n--- CALCULADORA ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    
    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            print("(Somar)")
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {n1 + n2:.2f}")
            
        elif opcao == 2:
            print("(Subtrair)")
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {n1 - n2:.2f}")
            
        elif opcao == 3:
            print("(Multiplicar)")
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {n1 * n2:.2f}")
            
        elif opcao == 4:
            print("(Dividir)")
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            if n2 == 0:
                print("Erro: divisão por zero!")
            else:
                print(f"Resultado: {n1 / n2:.2f}")
                
        elif opcao == 5:
            print("Saindo...")
        else:
            print("Opção inválida!")

    except ValueError:
        print("Entrada inválida! Digite apenas números.")
