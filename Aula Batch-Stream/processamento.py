# %%

import pandas as pds
import random
import time
# %%
# # Simulando batch (captura tudo)
# df = pd.read_csv(r'C:\Users\viniciussm\OneDrive - Votorantim\Documentos\Engenharia de dados\CursoEngenhariaDados\Aula Batch-Stream\vendas - Página.csv',
#                  sep=';')
# total_produtos = df.groupby('produto')['valor'].sum()
# print(total_produtos)

# %%
# Simulando stream


produtos = ['Camisa', 'Calça', 'Tênis']
total_produto = {}

for x in range(10):
    produto = random.choice(produtos)
    valor = random.randint(50, 201)
    total_produto[produto] = total_produto.get(produto, 0) + valor

    print(f'Nova venda: {produto} : {valor}')
    print(f'Total parcial: {total_produto[produto]} ')
    print('---')
    time.sleep(1)

print('#' * 30)
print('Total do dia')
print('Produto --> Valor')
for produto, valor in total_produto.items():
    print(f'{produto} --> {valor}')
print('#' * 30)

# %%
