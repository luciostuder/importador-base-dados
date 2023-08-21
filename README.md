# importador-base-dados

### Atualização da base de dados da OM com produtos existentes no fornecedor
1. na aplicação *Shopify*, para cada produto da Outra Música (OM) que exista na Base de Dados (BD) do fornecedor, colocar no campo SKU a referencia do catálogo do fornecedor. Isto irá relacionar ambas as entradas, permitindo posteriormente atualizar o preço.


### Atualização da BD da OM com base num novo ficheiro de CSV do fornecedor 
1. na aplicação *Shopify*, exportar a BD de produtos da OM, no formato *CSV - Comma Separated Values*
2. Com o Excel, abrir o ficheiro CSV. Passos:
    1. criar um novo ficheiro Excel
    2. no separador *Dados*, selecionar *importar dados*
    3. indicar o carater separador de valores (`,`, ou `;`) usado no ficheiro CSV
3. criar nova coluna (a primeira, 'A'), e colocar copia da coluna SKU.  
3. Com o Excel, abrir o ficheiro CSV do fornecedor. Passos idênticos ao número anterior.
4. no ficheiro do fornecedor, criar uma nova coluna (a primeira, 'A') chamada *handle*
5. aplicar a todas as células da coluna *handle* a formula: 
`=IF(ISNA(VLOOKUP(C6422,OM!A$1:B$5000,2,FALSE)),"",VLOOKUP(C6422,OM!A$1:B$5000,2,FALSE))`
onde:
    * `C2` é a celula do CSV do fornecedor onde está a referencia do produto (coluna `C`, linha `2`)
    * `OM` é o nome da pagina/ficheiro que contem o CSV da OM
6. eliminar as linhas que não tenham valores de handle 
6. gravar como CSV o ficheiro do fornecedor.
7. na aplicação *Shopify*, importar o ficheiro, selecionando a caixa de seleção "atualizar produtos com mesmo handle", para que ele reconheça que se pretende atualizar os produtos

<img width="451" alt="image" src="https://github.com/luciostuder/importador-base-dados/assets/42048382/3c3a41c0-1b55-484d-a8c9-25e8f5ca8c0b" style="text-align:center">

9. das colunas do ficheiro, selecionar apenas o handle e o preço
