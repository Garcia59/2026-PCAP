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
    [Escreva aqui, em uma linha, o que o seu jogo faz]
    '''

    titulo("MEU JOGO")

    # -------- DAQUI PARA BAIXO SEU: escreva SUA REGRA --------
    n = ler_numero("Escolha um numero de 1 a 5: ")
    print("Voce escolheu " + str(n) + ".")
    print("AQUI VAI A SUA REGRA: sortear, comparar, contar, decidir.")
    # -------- ATE AQUI --------

    linha()