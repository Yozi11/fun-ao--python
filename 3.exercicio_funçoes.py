import os

# Verifica se o número é maior que zero
def verifica_positivo_negativo(numero):
    if numero > 0:
        print("positivo") #Se for maior que zero, imprime 'Positivo'
    # Verifica se o número é menor que zero
    elif numero < 0:
        print("negativo")# Se for menor que zero, imprime 'Negativo'
    # Caso contrário, o número é igual a zero
    else:
        print("zero")  #Se for igual a zero, imprime 'Zero'

numero = int(input("digite o numero: "))

verifica_positivo_negativo(numero)                