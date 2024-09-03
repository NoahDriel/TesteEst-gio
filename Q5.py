# Função que recebe a string
def inverter_string(s):
    #String vazia para armazenar a string invertida
    s_invertida = ""
    
    # Looping iniciando da última posição da string até a posição 0 percorrendo de um em um)
    for i in range(len(s) - 1, -1, -1):
        #Inserido cada valor na string invertida
        s_invertida += s[i]
    
    return s_invertida

s = "liberdade"
s_invertida = inverter_string(s)
print(s_invertida)
