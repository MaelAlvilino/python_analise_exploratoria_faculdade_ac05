import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('CarPrice_Assignment.csv')
print(dados)

pares = [('curbweight', 'price'), ('wheelbase', 'price'), ('enginesize', 'price'),
         ('horsepower', 'price'), ('compressionratio', 'price')]

tabela_correlacoes = pd.DataFrame(columns=['Variáveis', 'Coeficiente de Correlação'])
for x, y in pares:
    coef_corr = np.corrcoef(dados[x], dados[y])[0, 1]
    
    tabela_correlacoes = pd.concat([tabela_correlacoes, pd.DataFrame({'Variáveis': [f'{x} vs {y}'],
                                                                     'Coeficiente de Correlação': [coef_corr]})],
                                   ignore_index=True)

    
    plt.scatter(dados[x], dados[y], label='Dados')
    m, b = np.polyfit(dados[x], dados[y], 1)
    plt.plot(dados[x], m*dados[x] + b, color='red', label='Linha de Ajuste')
    
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'Relação entre {x} e {y}')
    plt.legend()
    plt.show()


print(tabela_correlacoes)

indice_max_correlacao = tabela_correlacoes['Coeficiente de Correlação'].idxmax()
par_maior_correlacao = tabela_correlacoes.loc[indice_max_correlacao, 'Variáveis']

print(f"O par de variáveis com a maior correlação é: {par_maior_correlacao}")

indice_min_correlacao = tabela_correlacoes['Coeficiente de Correlação'].idxmin()
par_menor_correlacao = tabela_correlacoes.loc[indice_min_correlacao, 'Variáveis']

print(f"O par de variáveis com a menor correlação é: {par_menor_correlacao}")