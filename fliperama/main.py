# =============================================
# Arquivo:    main.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      [Matheus Felipe]
# Data:       2026.08.04
# Conceitos:  []
# =============================================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from modulos import ler_opcao
from placar import carregar_placar, salvar_placar

NOME_DO_DONO = 'MATHEUS.FELIPE'

OPCOES = ['0', '1', '2', '3', '9']

NOMES_DOS_JOGOS = [
    'Adivinhe o Numero',
    'Pedra-Papel-Tesoura',
    'Par ou Impar'
]

vezes_jogado = carregar_placar()

nome_jogador = input('Quem está jogando? ')


def mostrar_placar():
    titulo('PLACAR')

    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')


while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)

    print('Jogador: ' + nome_jogador)
    linha()

    mostrar_placar()

    linha()

    print('1 - Jogo Adivinhe o Número')
    print('2 - Pedra-Papel-Tesoura')
    print('3 - Par ou Impar')
    print('9 - Zerar o placar')
    print('0 - Sair do Fliperama')

    linha()

    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        salvar_placar(vezes_jogado)
        titulo('Ate a proxima!')
        break

    elif opcao == '9':
        vezes_jogado = [0, 0, 0]
        salvar_placar(vezes_jogado)
        print('Placar zerado!')

    else:
        indice = int(opcao) - 1

        if opcao == '1':
            jogar_adivinhe()

        elif opcao == '2':
            jogar_ppt()

        elif opcao == '3':
            jogar_parimpar()

        vezes_jogado[indice] = vezes_jogado[indice] + 1

        salvar_placar(vezes_jogado)

        arquivo = open('historico.txt', 'a')
        arquivo.write(
            nome_jogador + ' - ' + NOMES_DOS_JOGOS[indice] + '\n'
        )
        arquivo.close()