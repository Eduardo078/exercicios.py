numero_positivo = int(input("digite um numero inteiro e positivo: "))

soma = 0
for numero in range(numero_positivo +1):
    if numero % 2 != 0:
        print(numero)
        soma += numero
        
print(f"A soma dos numeros impares é {soma}")
        
        