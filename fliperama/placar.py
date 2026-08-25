# =================================================================
# ARQUIVO    : ppt.py (pasta fliperama)
# Conceitos  : Jogo com modulo, lista como tabela de nomes,funçao com retorno, operador % para dar a volta
# Base       : Jogo da Aula 17 (Atividade 11)
# Autor      : [Matheus Felipe]
# Data       : 2026.08,11
# ==================================================================

def carregar_placar():
    try:
        arquivo = open('placar.csv', 'r')

        linha = arquivo.readline()
        arquivo.close()

        valores = linha.strip().split(',')

        return [
            int(valores[0]),
            int(valores[1]),
            int(valores[2])
        ]

    except FileNotFoundError:
        return [0, 0, 0]


def salvar_placar(vezes_jogado):
    arquivo = open('placar.csv', 'w')

    arquivo.write(
        str(vezes_jogado[0]) + ',' +
        str(vezes_jogado[1]) + ',' +
        str(vezes_jogado[2])
    )

    arquivo.close()


def zerar_placar(vezes_jogado):
    vezes_jogado[0] = 0
    vezes_jogado[1] = 0
    vezes_jogado[2] = 0