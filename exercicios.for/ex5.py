entrada = input("Digite uma sequência de números inteiros separados por espaço: ")

# Divide a entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = [int(x) for x in numeros_str]

# Calcular a soma de todos os números
soma = sum(numeros)

# Agora você pode trabalhar com a lista de números inteiros
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
print(f"Soma de todos os números: {soma}")
