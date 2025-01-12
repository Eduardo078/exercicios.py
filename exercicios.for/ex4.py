numero_positivo = int(input("digite um numero inteiro e positivo: "))

if numero_positivo < 2:
    print("O numero não é primo")
else:
    for i in range(2,numero_positivo):
        if numero_positivo % i == 0:
            print("o número não é primo")
            break
    else:
        print(f"O numero {numero_positivo} é primo")
