# importador-base-dados

## preparação da base de dados da OM
1. descarregar CSV
2. abrir o ficheiro com Excel
3. para os produtos existentes na base de dados do fornecedor, colocar no CSV da OM desse produto, na coluna SKU, o valor da referencia.


## importação - atualização da BD da OM com base num novo ficheiro de CSV do fornecedor 
1. descarregar a base de dados em csv do fornecedor
2. abrir com excel
3. criar uma nova coluna chamada handle
4. aplicar a todas as céluas da coluna handle a formula: =VLOOKUP(C2,OM!A$1:B$5000,2,FALSE), onde:
    * C2 é a celula do CSV do fornecedor onde está a referencia do produto
    * OM é o nome da pagina que contem o CSV da OM
5. gravar novamente como CSV o ficheiro do fornecedor
6. importar o ficheiro para a aplicação, indicando no checkbox "handle", para que ele reconheça produtos a atualizar
