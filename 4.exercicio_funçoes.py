#cria uma funçao
def exibe_tabuada(numero):

    #laço que vai de 1  ate 10
    for i in range(1, 11):
        #mostra a multiplicação do numero
        print(f"{numero} x {i} = {numero * i}")
#solicita um numero ao usuario        
num = int(input("informe um numero para a tabuada: "))

#chama a funçao para exibir a tabuada
exibe_tabuada(num)
