frase = input("Digite uma frase: ")
letra = input("Digite a letra que deseja contar: ")

# Converte a frase para minúsculas para garantir a contagem correta
frase = frase.lower()
letra = letra.lower()

# Inicializa o contador
contador = 0

# Loop para percorrer cada caractere da frase
for caractere in frase:
    if caractere == letra:
        contador += 1

print(f"A letra '{letra}' aparece {contador} vezes na frase.")
