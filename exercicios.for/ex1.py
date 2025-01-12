numero_positivo = int(input("Digite um numero inteiro positivo: "))

soma = 0
for numero in range(numero_positivo + 1):
    print(numero)
    soma += numero
    
print(f"A soma é: {soma}")
    