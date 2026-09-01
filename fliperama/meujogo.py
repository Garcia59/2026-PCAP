# ============================================================
# ARQUIVO    : meujogo.py (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 23 - O jogo autoral do meu fliperama
# Autor      : [Matheus Felipe]
# Conceitos  : Reuso de modulo proprio, funcao sem retorno,
#              entrada validada. contagem de partidas
# ============================================================

from telas import titulo, linha
from modulos import ler_numero


def jogar_meujogo():
    """
    Jogo do foguete:
    desvie dos meteoros e tente fazer a maior pontuacao.
    """

    import pygame
    import random

    pygame.init()

    titulo("MEU JOGO - FOGUETE")

    # Tela
    LARGURA = 800
    ALTURA = 600

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Foguete - Desvie dos Meteoros")

    # Cores
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    CINZA = (120, 120, 120)

    # Foguete
    foguete = pygame.Rect(380, 500, 40, 60)
    velocidade = 7

    # Meteoros
    meteoros = []
    velocidade_meteoro = 5

    # Pontuacao
    pontos = 0
    fonte = pygame.font.Font(None, 36)

    relogio = pygame.time.Clock()
    rodando = True

    while rodando:

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Teclas
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] and foguete.left > 0:
            foguete.x -= velocidade

        if teclas[pygame.K_RIGHT] and foguete.right < LARGURA:
            foguete.x += velocidade

        # Criar meteoros
        if random.randint(1, 30) == 1:
            x = random.randint(0, LARGURA - 40)

            meteoro = pygame.Rect(x, -40, 40, 40)
            meteoros.append(meteoro)

        # Movimentar meteoros
        for meteoro in meteoros[:]:

            meteoro.y += velocidade_meteoro

            # Meteoro saiu da tela
            if meteoro.top > ALTURA:
                meteoros.remove(meteoro)
                pontos += 1

            # Colisao
            elif foguete.colliderect(meteoro):
                rodando = False

        # Fundo
        tela.fill(PRETO)

        # Foguete
        pygame.draw.polygon(
            tela,
            BRANCO,
            [
                (foguete.centerx, foguete.top),
                (foguete.left, foguete.bottom),
                (foguete.right, foguete.bottom)
            ]
        )

        # Meteoros
        for meteoro in meteoros:
            pygame.draw.circle(
                tela,
                CINZA,
                meteoro.center,
                20
            )

        # Pontuacao
        texto = fonte.render(
            "Pontos: " + str(pontos),
            True,
            BRANCO
        )

        tela.blit(texto, (20, 20))

        pygame.display.update()

        relogio.tick(60)

    pygame.quit()

    print("Fim de jogo!")
    print("Sua pontuacao foi:", pontos)

    input("Pressione Enter para voltar ao menu...")

    linha()
