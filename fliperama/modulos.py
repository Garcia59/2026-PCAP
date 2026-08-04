# =============================================
# Arquivo:    modulos.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      [Matheus Felipe]
# Data:       2026.08.04
# Conceitos:  []
# =============================================

def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ': ').strip()
    while resposta not in validas:
        print('Opcao Inválida! Tente Novamente.')
        resposta = input(mensagem + ': ').strip()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    numero = []
    for n in range(minimo, maximo + 1):
        numero.append(str(n))
    return int(ler_opcao(mensagem, numero))
