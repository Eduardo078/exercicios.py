numero_positivo = int(input("Digite um numero inteiro e positivo: "))

quantidade_de_pares = 0
for numero in range(numero_positivo +1):
    if numero % 2 == 0:
        print(numero)
        quantidade_de_pares += 1

print(f"A quanridade de numeros pares é: {quantidade_de_pares}")
