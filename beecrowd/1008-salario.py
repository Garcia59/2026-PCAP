'''
Problema: beecrowd | 1008
Data: 2026.04.09
Estudantes: Matheus Felipe Garcia
'''
# Objetivo: Escrever um programa que leia horas trabalhadas de funcionário e o valor que recebe por hora

# --- ANÁLISE (LIAC) ---
# Entrada: O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais
# Processamento: horas trabalhadas = horas * 1h total = receber por hora e calcular o salrio deste funcionario
# Saída: Imprima o número e o salário do funcionário

# Leitura das entradas - observe o enunciado: quantas variáveis e de qual tipo?
N = int(input())
H = int(float())
V = int(print())

# Calcule o salário - use o 1009 como referência de estrutura
SAL = N + H + V

# Saída - observe o formato exato e o número de casas decimais no enunciado
print(f"TOTAL = R$ {SAL}")