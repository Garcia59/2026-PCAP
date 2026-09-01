# =============================================
# Arquivo:    main.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      [Matheus Felipe]
# Data:       2026.08.04
# Conceitos:  [..]
# =============================================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
from meujogo import jogar_meujogo

NOME_DO_DONO = 'MATHEUS.FELIPE'

OPCOES = ['0', '1', '2', '3', '4', '5']

NOMES_DOS_JOGOS = [
    'Adivinhe o Numero',
    'Pedra-Papel-Tesoura',
    'Par ou Impar'
    'Jogar meujogo'
]


vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

nome_jogador = input('Quem esta jogando? ')


def mostrar_placar():
    titulo('PLACAR')

    for i in range(3):
        print(
            NOMES_DOS_JOGOS[i]
            + ': '
            + str(vezes_jogado[i])
            + 'x'
        )


while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)

    linha()

    print('[1] Adivinhe o Numero')
    print('[2] Pedra-Papel-Tesoura')
    print('[3] Par ou Impar')
    print('[4] Jogadores')
    print('[5] Meu Jogo')
    print('[0] Sair')

    linha()

    opcao = ler_opcao('Sua escolha', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo('Ate a proxima!')
        break

    elif opcao == '4':
        menu_jogadores(jogadores)

    elif opcao == '1':
        jogar_adivinhe()

        vezes_jogado[0] = vezes_jogado[0] + 1
        salvar_placar(vezes_jogado)

        arquivo = open('historico.txt', 'a')
        arquivo.write(
            nome_jogador
            + ' - '
            + NOMES_DOS_JOGOS[0]
            + '\n'
        )
        arquivo.close()

    elif opcao == '2':
        jogar_ppt()

        vezes_jogado[1] = vezes_jogado[1] + 1
        salvar_placar(vezes_jogado)

        arquivo = open('historico.txt', 'a')
        arquivo.write(
            nome_jogador
            + ' - '
            + NOMES_DOS_JOGOS[1]
            + '\n'
        )
        arquivo.close()

    elif opcao == '3':
     jogar_parimpar()

    vezes_jogado[2] = vezes_jogado[2] + 1
    salvar_placar(vezes_jogado)

    arquivo = open('historico.txt', 'a')
    arquivo.write(
        nome_jogador
        + ' - '
        + NOMES_DOS_JOGOS[2]
        + '\n'
    )
else: jogar_meujogo

arquivo.close()



input('Pressione Enter para voltar ao menu... ')