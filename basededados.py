import pandas as pd

tabela = pd.read_excel(r"C:\Users\rr\Downloads\Aula 1-20220510T201822Z-001\Aula 1\Exportar\Vendas - Dez.xlsx")
print(tabela)


faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print(faturamento)
print(quantidade)

