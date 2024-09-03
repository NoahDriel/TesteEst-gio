import json

# Função para carregar os dados de faturamento a partir de um arquivo JSON
def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as file:
        return json.load(file)
        
# Função para calcular os valores solicitados
def analisar_faturamento(dados):
    # Ignorar dias com faturamento zero
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)

    # Contar quantos dias tiveram faturamento acima da média mensal
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Exemplo de uso
dados_faturamento = carregar_faturamento('Arquivos_json\\Faturamento.json')
menor, maior, dias_acima = analisar_faturamento(dados_faturamento)

print(f"Menor faturamento do mês: R$ {menor:.2f}")
print(f"Maior faturamento do mês: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
