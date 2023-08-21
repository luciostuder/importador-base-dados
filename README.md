# importador-base-dados

### Atualização da base de dados da OM com produtos existentes no fornecedor
1. na aplicação *Shopify*, para cada produto da Outra Música (OM) que exista na Base de Dados (BD) do fornecedor, colocar no campo SKU a referencia do catálogo do fornecedor. Isto irá relacionar ambas as entradas, permitindo posteriormente atualizar o preço.


### Atualização da BD da OM com base num novo ficheiro de CSV do fornecedor 
1. descarregar ambos os ficheiros CSV a) de OM e b) do fornecedor. Guardar nesta pasta
1. abrir linha de comandos na pasta onde está o scripy python, e executar o comando `python atualiza_precos.py` 
1. na aplicação *Shopify*, importar o ficheiro, selecionando a caixa de seleção "atualizar produtos com mesmo handle", para que ele reconheça que se pretende atualizar os produtos
1. das colunas do ficheiro, selecionar apenas o handle e o preço

<img width="451" alt="image" src="https://github.com/luciostuder/importador-base-dados/assets/42048382/3c3a41c0-1b55-484d-a8c9-25e8f5ca8c0b" style="text-align:center">

