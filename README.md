# importador-base-dados

### Atualização da base de dados da OM com produtos existentes no fornecedor
1. em cada produto que exista na base de dados do fornecedor, colocar no campo SKU o valor da referencia do catálogo do fornecedor.


### Atualização da BD da OM com base num novo ficheiro de CSV do fornecedor 
1. exportar base de dados de produtos da OM, no formato CSV
2. abrir com Excel o ficheiro CSV da OM. Passos:
    * criar um novo ficheiro Excel
    * no separador *Dados*, selecionar *importar dados*
    * indicar o carater separador de valores (`,`, ou `;`) usado no ficheiro *CSV - Comma Separated Values* 
3. abrir com Excel o ficheiro CSV do fornecedor. Passos idênticos ao número anterior.
3. no ficheiro do fornecedor, criar uma nova coluna chamada `handle`
4. aplicar a todas as células da coluna handle a formula: `=VLOOKUP(C2,OM!A$1:B$5000,2,FALSE)`, onde:
    * C2 é a celula do CSV do fornecedor onde está a referencia do produto (coluna C, linha 2)
    * OM é o nome da pagina/ficheiro que contem o CSV da OM
5. gravar novamente como CSV o ficheiro do fornecedor
6. importar o ficheiro para a aplicação, indicando no checkbox "handle", para que ele reconheça produtos a atualizar
7. das colunas do ficheiro, selecionar apenas o handle e o preço
