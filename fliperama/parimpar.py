# =================================================================
# ARQUIVO    : ppt.py (pasta fliperama)
# Conceitos  : Jogo com modulo, lista como tabela de nomes,funçao com retorno, operador % para dar a volta
# Base       : Jogo da Aula 17 (Atividade 11)
# Autor      : [Matheus Felipe]
# Data       : 2026 08.11
# ==================================================================

from telas import titulo, linha
from modulos import ler_numero
import random


def jogar_parimpar():
    titulo('PAR OU IMPAR')

    numero = ler_numero('Digite um número: ')

    escolha = input('Você escolhe par ou impar? ').lower()

    computador = random.randint(0, 10)

    resultado = numero + computador

    print('Você escolheu:', escolha)
    print('Computador jogou:', computador)
    print('Resultado:', resultado)

    linha()

    if resultado % 2 == 0:
        resultado_paridade = 'par'
    else:
        resultado_paridade = 'impar'

    print('Resultado foi:', resultado_paridade)

    if escolha == resultado_paridade:
        print('Você ganhou!')
    else:
        print('Você perdeu!')

    linha()