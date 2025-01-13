frase = input("Digite uma frase: ").lower()

#dicionário para contar as vogais
contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Percorrendo cada caractere da frase
for vogal in frase:
    if vogal in contagem_vogais:  # Verifica se o caractere é uma vogal
        contagem_vogais[vogal] += 1

# Calcula o total de vogais
total_vogais = sum(contagem_vogais.values())


print(f"Total de vogais: {total_vogais}")
for vogal, quantidade in contagem_vogais.items():
    print(f"{vogal.upper()}: {quantidade}")
