# Fliperama em C++ (MeuApp v4.0)

## O que é
O Fliperama é um programa que permite cadastrar jogadores, listar apelidos e jogar o jogo de adivinhar números, contando as partidas de cada jogador

Ele foi desenvolvido como projeto da disciplina 2026-PCAP, utilizando C++ para organizar os jogos e salvar os dados em arquivos.

## Como compilar e rodar
```bash
g++ -Wall fliperama.cpp -o fliperama
./fliperama
```

## Arquivos
- **fliperama.cpp:** contém o código principal, menus, cadastro de jogadores e o jogo.
- **jogadores.csv:** guarda os apelidos dos jogadores e a quantidade de partidas de cada um.

## C x C++: o que mudou

| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| Guardar um jogador | strcpy(apelidos[qtd], novo) (l.65) | apelidos.push_back(novo) (l. 100) |
| Comparar apelidos | strcmp(...) == 0 (l.55) | apelidos[i] == procurado (l. 62) |
| A função que cadastra | int cadastrar(..., int qtd) (l.87) | void cadastrar(...) (l. 93) |
| Passar os vetores por referência | — | void cadastrar(vector<string> &apelidos, ...) (l. 93) |

## O que o C++ decidiu por mim
Em C, era necessário controlar manualmente o espaço dos dados e usar funções como strcpy. Em C++, o vector aumenta automaticamente quando adicionamos novos jogadores com push_back.

Além disso, a string facilita o armazenamento e a comparação dos apelidos.

## Autoavaliação

| Critério | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilação e Git | B | fliperama.cpp, compilação |
| 2. Cadastro: vetores e referência | B | fliperama.cpp, linhas 93 a 103 |
| 3. Jogo e partidas | B | fliperama.cpp, linhas 106 a 140 |
| 4. Persistência | B | fliperama.cpp, linhas 69 a 91 e 165 |
| 5. Documentação e comparação | B | README.md e comparação C x C++ |