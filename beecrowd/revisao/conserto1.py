# Conserto 1: trecho do "Adivinhe o Numero" (Aula16)
print("=== ADIVINHE O NUMERO ====")
segredo = 7
palpite = input("Digite um numero de 1 a 10:")
if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era", segredo)