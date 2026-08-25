# =============================================
# Arquivo:    telas.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      [Matheus Felipe]
# Data:       2026.08.04
# Conceitos:  [.]
# =============================================

# Definição da Moldura Caracteres e Tamanho
CAR = '#'
TAM = 60

# Função para desenha uma linha na tela
def linha():
    print(CAR * TAM)

# Função para desenha um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()
