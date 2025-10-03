import os
os.system("cls")

#função com passagem de parametros.

#crinado uma função.

def saudacao(nome, idade,altura,peso):
    print(f"ola, {nome}! Bem-vindo(a)! ")
    print(f"sua idade e {idade} anos .")
    print(f"digite seu altura:{altura}.")
    print(f"digite seu peso: {peso}")

print("solicitando dados. ")
nome = input("digite o seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))            
#chamando a função.;

 
saudacao(nome,idade,altura,peso)        