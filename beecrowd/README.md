🔢 Par ou Ímpar
​Jogo de Par ou Ímpar feito em Python na disciplina PCAP (Aula 18). Você joga contra o computador em uma melhor de 5 rodadas, com placar.​

▶️ Como jogar
Abra o terminal na pasta do jogo.
Rode: python par_impar.py
A cada rodada, escolha a aposta (par ou ímpar) e um número de 0 a 5.
Ao fim das 5 rodadas, o programa mostra o placar final.​
⚙️ Como funciona (resumo)
A cada rodada o computador sorteia um número (random.randint) e lê o seu. A aposta é limpa (.lower().strip()) e validada (in) antes de usar. A soma dos dois números define a paridade com o operador % (resto). Uma função decide quem venceu e o programa soma os pontos das 5 rodadas.​

🧠 O que eu pratiquei
Operador de resto (%): descobrir se a soma é par ou ímpar
Funções (def/return): isolar a regra do jogo (quem venceu)
random.randint: sortear o número da máquina
int(input()): ler o número do jogador
Métodos de texto (.lower().strip()) e validação com in: tratar a aposta
Repetição (for): jogar as 5 rodadas e manter o placar​
🎯 Autoavaliação
Conceito pretendido: [ B ]​Justificativa (cite arquivo e linha de cada critério):

O jogo funciona ...........: par_impar.py, linhas 1 a 34
Funções e operador % .......: par_impar.py, linha 7 (verificar_vencedor, soma % 2)
Documentação e Git .........: este README + commits no GitHub
Extensão/originalidade .....: par_impar.py, linha 34 (melhor de 5 placar de vitorias e derrotas)​Autor: [Matheus Felipe]
​
Jogo de Par ou Ímpar feito em Python na disciplina PCAP (Aula 18).
Você joga contra o computador em uma melhor de 5 rodadas, com placar.
​