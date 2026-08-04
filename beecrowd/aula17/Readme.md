# Entrada

# linha32 jogada_jogador = input("Sua jogada: ").lower().strip()
# linha32 input
# linha32 .lower

# Saida

# linha29 print("--- Rodada", rodada, "---")
# linha40 print("🏆 Você ganhou a rodada!")
# linha45 print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)

# Operador

# linha12 jogador == maquina
# linha33 jogada_jogador not in opcoes
# linha35 pontos_maquina = pontos_maquina + 1

# Sub-Rotina

# linha10 def resultado(jogador, maquina):
# linha20 return "maquina"
# linha37 quem = resultado(jogada_jogador, jogada_maquina)

# Condição

# linha12 if jogador == maquina:
# linha33 if jogada_jogador not in opcoes:
# linha39 elif quem == "jogador":

# Repetição

# linha28 for rodada in range(1, 6):
# linha29 print("--- Rodada", rodada, "---")
# linha30 jogada_maquina = random.choice(opcoes)

# Variaves 

# linha23 opcoes = ["pedra", "papel", "tesoura"]
# linha24 pontos_jogador = 0
# linha25 pontos_maquina = 0