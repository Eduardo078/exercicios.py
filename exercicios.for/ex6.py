numero_positivo = int(input("digite um numero inteiro e positivo: "))

contagem_par = 0
contagem_impar = 0
for numero in range(numero_positivo +1):
    if numero % 2 == 0:
        contagem_par += 1
    else:
        contagem_impar +=1
print(f"Existem {contagem_par} numeros pares, e {contagem_impar} numeros impares.")