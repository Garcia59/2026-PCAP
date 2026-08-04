'Fundamentos de Programação'
# 1. Variáveis e tipos de dados

#    Variáveis guarda um valor espesifico que o software precisa usar . tambem serve para achar o valor guardado de forma mais rapida
#     1 .Exmplos e Variaveis:

print(nome = "matheus")
print(idade = 15)
print(altura = 1.73)
print(Boolean = True)

#     2. tipos de variaveis
# String (texto)
# Inteiro (Número inteiro)
# Float (Numero Decimal)
# Boolean (Verdadeiro ou Falso V/F)

# 2. Operadores 

# Operadores são simbolos que usamos para criar calculos tambem comparar valores 
# Servem para fazer contas básicas.

# Exmplo:
# + (Adição): Soma dois valores.
# - (Subtração): Subtrai um valor do outro.
# * (Multiplicação): Multiplica os valores.
# / (Divisão): Divide os valores.

a = 10
b = 3

print(a + b)   # 13
print(a % b)   # 1


# 3. Entrada de dados


# A entrada de dados é a forma como um programa recebe informações Em Python, isso é feito principalmente com a função input().

variavel = input("Olá")

nome = input("Matheus")

print("Olá,", "matheus" )


# 4. Saída de dados


# saída de dados é a forma como um programa exibe informações na tela para o usuário. Em Python, a saída de dados é feita principalmente com a função print().
print("Olá, mundo")
# mostrando uma mensagem 
print("Olá, mundo!")

nome = "Matheus"
print(nome)
# Saida: Matheus


# 5. Estrutura de Repetição

# estruturas de repetição permitem executar um mesmo bloco de código várias vezes  evitando a repetição de comandos. Em Python as principais estruturas de repetição são for e while.
# A estrutura for é utilizada quando sabemos quantas vezes o bloco de código será repetido.
for variavel in sequencia:
    # bloco de código
# contagen de 1 a 5
# for i in range(1, 6):
    print (i)
# saida
1
2
3
4
5



# 6. Estrutura de Condição

# estruturas de condição permitem que um programa tome decisões com base em uma condição. Em Python, as principais estruturas condicionais são if, if...else e if...elif...else.
# A estrutura if executa um bloco de código somente se a condição for verdadeira.
if condicao:
    # bloco de código
# vendo a idade 
 idade = 15

if idade >= 18:
    print("Você é maior de idade.")




