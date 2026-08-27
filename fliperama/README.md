## Fliperama do Matheus Felipe

Um fliperama de terminal com tres jogos, placar que nao esquece e
cadastro de jogadores. Projeto da disciplina PCAP, 1 anao do Tecnico
em Informatica do IFPR.

## O que ele faz

- Tres jogos pelo menu: Adivinhe o Numero, Pedra-Papel-Tesoura e Par ou Impar
- Placar que conta quantas vezes cada jogo foi jogado e continua contando
depois de fechar o programa 
-Cadastro de jogadores: cadastrar, listar, alterar e excluir

## Como rodar

'''
cd fliperama
python3 main.py
'''

## Os arquivos

- `main.py` - o gabinete: menu, placar e chamadas
- `telas.py` - ferramentas visuais
- `modulos.py` - ferramentas de logica: as tres funcoes que perguntam e conferem
- `placar.py` - quantas partidas cada jogo teve
- `jogadores.py` - quem sao os jogadores
- `adivinhe.py`, `ppt.py`, `parimpar.py` - um arquivo por jogo
- `placar.csv` e `jogadores.csv` - os dados, que nascem sozinhos

A funcao `ler_texto` ficou no `modulos.py` porque

## De onde ele veio

- Aula 20: os tres jogos viraram um programa so, com modulos e menu
- Aula 21: entrou o Pedra-Papel-Tesoura e o placar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operacoes
- Aula campo em branco: o projeto documentado

## O que ainda nao funciona

- Nome com virgula quebra a linha do arquivo, porque a virgula e o separador.

## Autoavaliacao

Conceito que eu acho que a minha entrega vale: [ B  acredito que um B estou me esforsando des do inicio dessas aulas]

### Mapa do projeto: onde esta cada coisa

| O que | Arquivo | Funcao |
|---|---|---|
| Adivinhe o Numero | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Impar | `parimpar.py` | `jogar_parimpar` |
| [Jogo meu autoral fliperama] | `meujogo.py` | `jogar_meujogo` |
| Cadastro de jogadores | `jogadores.py` | `menu_jogadores` |
| Ranking Top 10 | `jogadores.py` | `listar` |
| Placar que sobrevive | `placar.py` | `salvar_placar`, `carregar_placar` |

### Criterio por criterio: o nivel e a prova

| Criterio | Nivel | Onde esta a prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura e registro | [B] | [arquivo, linha] |
| 2. As quatro operacoes | [B] | [arquivo, linha] |
| 3. Busca e indice | [B] | [arquivo, linha] |
| 4. Persistencia e primeira execucao | [B] | [arquivo, linha] |
| 5. Documentacao e autoavaliacao | [B] | [arquivo, linha] |
| 6. Jogo autoral e reuso | [B] | [arquivo, linha] |

### Usei IA

[ use para me ajudar a organizar a documentacao, entender os erros do codigo, nao apenas copiei olhei li para aprender a lidar quando acontecer esse erros novamentes]