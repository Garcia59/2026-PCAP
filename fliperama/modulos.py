# =============================================
# Arquivo:    modulos.py (pasta fliperama)
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      [Matheus Felipe]
# Data:       2026.08.04
# Conceitos:  [Reaproveitamento, validacao, funcao que chama  funcao]
# =============================================

def ler_opcao(mensagem, validas):
    # So devolve quando a resposta estiver na lista de validas.
    resposta = input(mensagem + ': ').strip()
    while resposta not in validas:
        print('Opcao Invalida! Tente Novamente.')
        resposta = input(mensagem + ': ').strip()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    # Monta a lista de numeros aceitos e reaproveita a ler_opcao
    numero = []
    for n in range(minimo, maximo + 1):
        numero.append(str(n))
    return int(ler_opcao(mensagem, numero))


def ler_texto(mensagem):
    # So devolve quando o texto nao estiver vazio.
    resposta = input(mensagem + ': ').strip()
    while resposta == '':
        print('Nao pode ficar em branco! Tente de novo.')
        resposta = input(mensagem + ': ').strip()
    return resposta

def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print('Digite um numero valido!')