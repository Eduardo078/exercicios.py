inicio = int(input("Digite o primeiro numero (inteiro e positivo): "))
fim = int(input("Digite o ultimo numero (inteiro e positivo): "))

soma = 0

for numero in range(inicio, fim +1):
    if numero % 3 == 0:
        soma += 1
print(f"Existem {soma} numeros dentro do intervalo quee SÃO multiplos de 3")