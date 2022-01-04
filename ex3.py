import json

with open("dados.json") as file:
    vetor = json.load(file)

menor = min(map(lambda x: float(x['valor']), vetor))
print(f'• O menor valor de faturamento ocorrido em um dia do mês: {menor}')

maior = max(map(lambda x: float(x['valor']), vetor))
print(f'• O maior valor de faturamento ocorrido em um dia do mês: {maior}')

a = []

for i in vetor:
    if(i["valor"] != 0 ):
        a.append(i)

soma = sum(map(lambda x: float(x['valor']), a))
count = len(a)
media = soma / count


quantidade = sum(map(lambda x: 1 if int(x['valor']) > media else 0, a))
print(f'• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {quantidade}')

