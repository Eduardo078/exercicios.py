frase = input("Digite uma frase: ")

#Separa a frase em palavras
palavras = frase.split()

contagem_vogais = 0
contagem_consoantes = 0

# Define as vogais
vogais = 'aeiou'


for palavra in palavras:
    # Verifica se a primeira letra é uma vogal
    if palavra[0].lower() in vogais:
        contagem_vogais += 1
    else:
        contagem_consoantes += 1


print(f"Total de palavras: {len(palavras)}")
print(f"Palavras começando com vogais: {contagem_vogais}")
print(f"Palavras começando com consoantes: {contagem_consoantes}")
