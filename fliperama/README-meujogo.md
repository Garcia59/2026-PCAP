# [Jogo autoral do meu fliperama]

Jogo autoral do meu fliperama. Abre pela opcao [5] do menu.
Autor: [Matheus Felipe]

## A regra

[o Jogador escolhe um numero e depois aparece uma lista do numero 1 a 4 1 soma 2 subtracao 3 multiplicacao 4 divisao.]

## Como jogar

1. Dentro. da pasta `fliperama`, rode `python3 main.py`.
2. Escolha a opcao `[5]` no menu.
3. [Apos clicar a opcao [5] vc pode cadastrar jogador excluir jogador renomear nome.]

## O que eu reusei do projeto, e onde

| Peca | De qual modulo | Onde eu uso | Para que serve ali |
|---|---|---|---|
| `titulo()` | `telas.py` | `meujogo.py`, linha [16] | desenha a testeira do jogo |
| `linha()` | `telas.py` | `meujogo.py`, linha [24] | fecha a tela no fim da partida |
| `ler_numero()` | `modulos.py` | `meujogo.py`, linha [20] | pede o numero e recusa fora do intervalo |
| contagem da partida | `placar.py` | `main.py`, linha [] | soma 1 em `vezes_jogado` a cada partida |

[Se voce tambem usou a `buscar` do `jogadores.py` para perguntar quem
vai jogar, acrescente uma linha aqui dizendo onde.]

## Exemplo de execucao

```
[#############################################
                FLIPERAMA DO MATHEUS                
##############################################
=== Calculadora ===
Digite o primeiro numero:
Digite o segundo numero:
##############################################
[1] Adivinhe o Numero
[2] Pedra-Papel-Tesoura
[3] Par ou Impar
[4] Jogadores
[5] Meu Jogo
[0] Sair
##############################################]
```

## O que ainda nao funciona

- [A regra do meu jogo ainda nao foi implementada. Por enquanto, o programa recebe um numero de 1 a 5 e mostra a escolha feita pelo jogador.
A mensagem AQUI VAI A SUA REGRA: sortear, comparar, contar, decidir. ainda precisa ser trocada pela regra final do jogo.
No main.py, a parte que conta as partidas de Par ou impar precisa ser corrigida, porque esta com a indentacao errada e ficou fora do elif opcao == '3':.]