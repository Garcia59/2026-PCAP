# Fliperama em C (MeuApp v3.0)

## O que e 
[duas linhas suas: o que o programa faz e de onde ele veio]

## Como compilar e rodar
gcc -Wall fliperama.c -o fliperama
./fliperama

## Arquivos
- fliperama.c [uma linha]
- jogadores.csv [uma linha: o que cada coluna guarda]

## Python x C: o que mudou
| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
| guardar um jogador | jogadores.append(novo) (l. 15) | strcpy(apelidos[qtd], novo) (l. 68) |
| comparar apelidos | == (l. 18) | strcmp(...) == 0 (l. 50) |
| abrir sem arquivo | exists(ARQUIVO) (l. 22) | fopen == NULL (l. 132) |


## O que o C me obrigou a decidir
[No Python As listas crescem sozinhas conforme vais adicionando itens com o .append(). Nem precisas de pensar no limite porque a propria linguagem trata de arranjar mais espaco na memoria.]


## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | |A |fliperama.c, l. 1-15 (inclusao de bibliotecas e constantes #define)
| 2. Cadastro: menu, funcoes e vetores | |A |fliperama.c, l. 57-71 (cadastrar) e l. 143-152 (mostrar_menu)
| 3. Jogo e partidas | |A |fliperama.c, l. 86-117 (jogar_adivinhe)
| 4. Persistencia | |A |fliperama.c, l. 119-141 (salvar e carregar)
| 5. Documentacao e comparacao | |A |README.md (ou relatorio de comparacao Python x C)