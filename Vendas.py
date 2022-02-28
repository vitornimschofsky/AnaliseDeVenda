#logica de programação

#passo 0 - entender o desafio

#passo 1 - percorrer todos os arquivos da pasta base de dados(pasta vendas)

import plotly.express as px
import os
import pandas as pd
from pprint import pprint



lista_arquivos = os.listdir("C:/Users/Vitor/Desktop/Python/AnaliseEmpresa/Vendas")
pprint(lista_arquivos)

tabela_total = pd.DataFrame()

#passo 2 - importar as bases de dados de vendas
for arquivos in lista_arquivos:
    #se tem "Vendas" no nome do arquivo, então
    if "Vendas" in arquivos:       
    #importar um arquivo
        tabela = pd.read_csv(f"C:/Users/Vitor/Desktop/Python/AnaliseEmpresa/Vendas/{arquivos}")
        tabela_total = tabela_total.append(tabela)

#passo 3 - tratar/compilar as bases de dados
pprint(tabela_total)

#passo 4 - calcular o produto mais vendido (em quantidade)
tabela_produto = tabela_total.groupby('Produto').sum()
#Mostrar a quantidade vendida em ordem crescente
tabela_produto = tabela_produto[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=True)
pprint(tabela_produto)



#passo 5 - calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
pprint(tabela_total)

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=True)
pprint(tabela_faturamento)

#passo 6 - calcular loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard

tabela_maiorloja = tabela_total.groupby('Loja').sum()
tabela_maiorloja = tabela_maiorloja[['Faturamento']].sort_values(by='Faturamento', ascending=False)
pprint(tabela_maiorloja)

grafico = px.bar(tabela_maiorloja, x=tabela_maiorloja.index , y='Faturamento')
grafico.show()
