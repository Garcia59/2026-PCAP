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
from modulos import ler_opcao

NOME_DO_DONO = 'MATHEUS.FELIPE'
OPCOES = ['0', '1', '2']
NOMES_DOS_JOGOS = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar']
vezes_jogado = [0, 0, 0]


def mostrar_placar():
    titulo('PLACAR')

    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')


while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)

    print('1 - Jogo Adivinhe o Número')
    print('2 - Pedra-Papel-Tesoura')
    print('0 - Sair do Fliperama')

    linha()

    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        mostrar_placar()
        titulo('Ate a proxima!')
        break

    elif opcao == '1':
        jogar_adivinhe()

    elif opcao == '2':
        jogar_ppt()

    indice = int(opcao) - 1
    vezes_jogado[indice] = vezes_jogado[indice] + 1