# ============================================================
# ARQUIVO    : meujogo.py (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 23 - O jogo autoral do meu fliperama
# Autor      : [Matheus Felipe]
# Conceitos  : Reuso de modulo proprio, funcao sem retorno,
#              entrada validada, contagem de partidas
# ============================================================

from telas import titulo, linha       # gaveta VISUAL
from modulos import ler_numero        # gaveta de ENTRADA validada


def jogar_meujogo():
    '''
    [ele lista cadastra jogadores e lista voce pode jogar parimpar , ppt]
    '''

    titulo("MEU JOGO")

    # -------- DAQUI PARA BAIXO SEU: escreva SUA REGRA --------
    n = ler_numero("Escolha um numero: ")
    print("Voce escolheu " + str(n) + ".")
    print("AQUI VAI A SUA REGRA: sortear, comparar, contar, decidir.")
    # -------- ATE AQUI --------
# Calculadora Simples em Python

print("=== Calculadora ===")

# Entrada dos numeros
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

# Escolha da operacao
print("\nEscolha a operacao:")
print("1 - Soma (+)")
print("2 - Subtracao (-)")
print("3 - Multiplicacao (*)")
print("4 - Divisao (/)")

opcao = input("Digite a opcao (1/2/3/4): ")

# Calculo
if opcao == "1":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif opcao == "2":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif opcao == "3":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: divisao por zero nao e permitida!")

else:
    print("Opcao invalida!")

    linha()