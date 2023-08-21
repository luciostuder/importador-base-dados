# importador-base-dados

### Atualização da base de dados da OM com produtos existentes no fornecedor
1. em cada produto que exista na base de dados do fornecedor, colocar no campo SKU o valor da referencia do catálogo do fornecedor.


### Atualização da BD da OM com base num novo ficheiro de CSV do fornecedor 
1. exportar base de dados de produtos da OM, no formato *CSV - Comma Separated Values*
2. abrir, com o Excel, o ficheiro CSV. Passos:
    1. criar um novo ficheiro Excel
    2. no separador *Dados*, selecionar *importar dados*
    3. indicar o carater separador de valores (`,`, ou `;`) usado no ficheiro CSV 
3. abrir, com o Excel, o ficheiro CSV do fornecedor. Passos idênticos ao número anterior.
4. no ficheiro do fornecedor, criar uma nova coluna chamada `handle`
5. aplicar a todas as células da coluna handle a formula: `=VLOOKUP(C2,OM!A$1:B$5000,2,FALSE)`, onde:
    * C2 é a celula do CSV do fornecedor onde está a referencia do produto (coluna C, linha 2)
    * OM é o nome da pagina/ficheiro que contem o CSV da OM
6. gravar novamente como CSV o ficheiro do fornecedor
7. importar o ficheiro para a aplicação, indicando no checkbox "handle", para que ele reconheça produtos a atualizar
8. das colunas do ficheiro, selecionar apenas o handle e o preço
