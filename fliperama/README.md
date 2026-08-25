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
