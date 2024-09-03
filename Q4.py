SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
DISTR = 180759.98

#Função que recebe o valor
def  Valor_Perc(v): 
    #Calculo do percentual, valor v sobre o total vezes 100
    perc = (v/DISTR)*100 
    return perc  

#Gera o valor pec arredondado para duas casas decimais com o símbolo de porcentagem 
print(f'{Valor_Perc(OUTROS):.2f}%')

