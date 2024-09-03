#definindo a sequencia de fibonacci
def número_fibonacci(num):
    #Começa a partir do zero
    if num < 0:
        return False
    #Sequencia começa com 0 e 1
    seq = [0, 1]
    #Repetição enquanto o número anterior for menor que num
    while seq[-1] < num:
        #Adiciona um número ao final da lista que é a soma da posição -1 e -2
        seq.append(seq[-1] + seq[-2])
    #Retorna se o número está na sequencia com True ou False    
    return num in seq

inp = 21

#print(número_fibonacci(inp))

#Testa se for verdadeiro else se for falso
if número_fibonacci(inp):
    print(f"{inp} pertence à sequência de Fibonacci.")
else:
    print(f"{inp} NÃO pertence à sequência de Fibonacci.")


