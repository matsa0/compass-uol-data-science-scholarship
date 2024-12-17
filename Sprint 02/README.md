
<h1 align="center">
    <strong>SPRINT 02</strong>
</h1>

# 📝 Exercícios

###  ➣ Curso: SQL para Análise de Dados: Do básico ao avançado


1. ...
[Resposta Ex1.](exercicios/ex1.txt)


2. ...
[Resposta Ex2.](exercicios/ex2.txt)




# 🔎 Evidências

### ➣ Curso: Estatística para Análise de Dados com Python

- **Seção 3: Preparação, organização e estruturação dos dados**<br>
    A seção 3 nos fornece um primeiro contato 
    com o dataset ENEM do ano de 2019. Porém, 
    como o dataset é muito grande por abranger 
    o país inteiro, para fins didáticos, 
    foram feitos uma **série de tratamentos**, 
    para que o dataset se tornasse mais intuitivo
    para o aprendizado, organizado e 
    **limitadoao estado de São Paulo**.
    
    - Exclusão das colunas que não fazem sentido 
    em nossa análise:

        ![Evidência 01](./evidencias/curso_estatistica_para_analise_de_dados/curso_estatistica_para_analise_de_dados/sec03/exclusao_de_colunas.png)
    
    - Verificação da quantidade de valores nulos 
    para as notas respectivas as matérias do ENEM. Tratamento através da presença nos dois dias da prova, com `TP_PRESENCA_CH == 1` e `TP_PRESENCA_CN == 1`. Isso elimina valores nulos já que a ausência é contada se o valor das variáveis forem 0:  
        
        ![Evidência 02](./evidencias/curso_estatistica_para_analise_de_dados/sec03/verificacao_e_tratamento_nulos.png)
        

    Uma dos primeiros elementos ao se analisar o dataset, é tratar de suas colunas e linhas. Isso inclui, **renomear, reposicionar, excluir** e dentre outras operações.
    - Renomeação das colunas entre colchetes; 
    O valor antes do caractere ':' representa o 
    antigo nome e após, o novo nome da coluna:

        ![Evidência 03](./evidencias/curso_estatistica_para_analise_de_dados/sec03/renomeacao_de_colunas.png)

    - Renomeação das linhas de uma coluna:

        ![Evidência 04](./evidencias/curso_estatistica_para_analise_de_dados/sec03/renomeacao_linhas.png)

    Além disso, nessa seção aprendemos a realizar 
    alguns **filtros** e utilizar de 
    funcionalidades do Pandas como `loc`, `iloc`,
    `query`que vão proporcionar melhores 
    compreensões sobre o dataset.
    - Separando os candidatos em treineiros e 
    vestibulandos com `loc`:

        ![Evidência 05](./evidencias/curso_estatistica_para_analise_de_dados/sec03/separacao_treineiros_e_vestibulando.png)
    
    - Consulta da quantidade de notas 0.0 em 
    Matemática com uma `query`:

        ![Evidência 06](./evidencias/curso_estatistica_para_analise_de_dados/sec03/utilizando_query.png)

- **Seção 4: Fundamentos de estatística**<br>
    A seção 4 introduz conceitos muito utilizados
    de estatística para análise de dados, 
    como os diferentes tipos de amostragem 
    **(aleatória, sistemática, estratificada, por conglomerado)**, **distribuição de frequência** 
    e sua visualização a partir de gráficos, 
    **medidas de dispersão**, **outliers** e 
    visualização através do Boxplot. 

    - Amostra aleatória simples permite coletar 
    uma fração (`sample`) da população total. 
    Utiliza-se o seed para que a amostra seja 
    fixa, pois não é interessante uma amostra 
    que se modifica a cada execução. 

        ![Evidência 07](./evidencias/curso_estatistica_para_analise_de_dados/sec04/amostra_aleatoria_simpels.png)

    - Amostra por conglomerado permite a a divisão 
    da população em grupos, que representa a 
    amostra. No caso abaixo, cada valor '1' que 
    é gerado aleatoriamente pelo `np.random.choice` 
    indica que o grupo deve ser incluido.

        ![Evidência 08](./evidencias/curso_estatistica_para_analise_de_dados/sec04/amostra_conglomerado.png)

    - Amostra estratificada realizada sobre as 
    raças presentes no dataset. Uma fração de 
    amostra é coletada de cada raça e depois 
    concatenada, formando a amostra estratificada.

        ![Evidência 09](./evidencias/curso_estatistica_para_analise_de_dados/sec04/amostra_estratificada1.png)
        ![Evidência 10](./evidencias/curso_estatistica_para_analise_de_dados/sec04/amostra_estratificada2.png)

    - Visualização dos outliers: O `Boxplot` é 
    muito utilizado para visualização de outliers. 
    No exemplo abaixo, é feita uma análise das 
    notas de redação do enem do estado de São 
    Paulo para cada tipo de escola. Os pontos 
    no gráfico representam os 'valores atípicos'.

        ![Evidência 11](./evidencias/curso_estatistica_para_analise_de_dados/sec04/boxplot_para_outliers.png)
    
    - Tratamento dos outliers: No exemplo abaixo
    os `outliers` são removidos a partir de seus 
    valores mínimos e máximos, que são as retas 
    dos bigodes do Boxplot.

        ![Evidência 12](./evidencias/curso_estatistica_para_analise_de_dados/sec04/remocao_de_outliers.png)


- **Seção 5: Estatística probabilística para análise de dados**<br>
    A seção 5 introduz o conceito da probabilidade 
    relacionada a análise de dados. A estatística
    probabilística abrange a probabilidade de não
    ocorrer um evento, interseção de eventos, 
    probabilidade condicional e diversos outros 
    conceitos.

    Além disso, a seção abrange a probabilidade
    de distribuição discreta e contínuas e para
    finalizar, testes de normalidade.

    - Exemplo de probabilidade condicional, que 
    representa a probabilidade de um **evento A** 
    **condicionado a um evento B ocorrer**. Neste caso,
    a probabilidade de uma pessoa do dataframe ser
    **mulher e parda**.

        ![Evidência 13](./evidencias/curso_estatistica_para_analise_de_dados/sec05/probabilidade_condicional.png)

    - A distribuição analisa a provavilidade de 
    se obter 2 resultados. Abaxo, é testado a
    probabilidade de retirar uma `quatro mulheres
    num total de 10 amostras`.

        ![Evidência 14](./evidencias/curso_estatistica_para_analise_de_dados/sec05/distribuicao_binomial.png) 

    - O `Q-Q plot` nos permite visualizar graficamente
    se uma amostra possui distribuição normal
    através de sua **linha vermelha**.

        ![Evidência 15](./evidencias/curso_estatistica_para_analise_de_dados/sec05/analisando_normalidade.png)


    - O Q-Q plot abaixo indica a distribuição das notas de
    redação de um colégio aleatório. Como o gráfico não
    explicita exatamente se a distribuição é normal,
    um teste Shapiro-Wilk é realizado. Como o seu p-value
    é maior que 0.05, a sua distribuição pode ser considerada
    normal.

        ![Evidência extra](./evidencias/curso_estatistica_para_analise_de_dados/sec05/teste_normalidade_2.png)

- **Seção 6: Fundamentos da estatística para inferencial para análise de dados**<br>
    A seção 6 aborda diversos conceitos relacionados
    à estatística inferencial, no sentido de se
    ter uma hipótese a analisar. Diversos testes
    de hipótese são trabalhados como o **Teste Z, Teste T
    Correlação e Regressão Linear e denrte outros
    fatores.**

    - `Teste Z:` No exemplo abaixo, foi comparado
    a média das notas do colégio aleatório de
    São Paulo com a média das notas de todos os 
    colégios de SP. Com o `intervalo de confiança
    de 95% (significância de 0,05)`, aceita-se a 
    `hipótese alternativa` que o **colégio aleatório
    possui médias diferentes do que do estado de
    São Paulo.**

        ![Evidência 16](./evidencias/curso_estatistica_para_analise_de_dados/sec06/teste_z.png)

    - `Teste T:` O Teste T foi utilizado em outro
    colégio aleatório, porém a amostra utilizada
    era menor que 30, pois o Teste T possui maior
    precisão para amostras menores. Aceita-se a
    `hipótese alternativa` que o **colégio aleatório
    possui médias diferentes do que do estado de
    São Paulo.**

        ![Evidência 17](./evidencias/curso_estatistica_para_analise_de_dados/sec06/teste_t.png)

    - `Teste Mann Whitney:` Esse teste é utilizado para
    amostras `não paramétricas, ou seja, independentes`.
    No caso abaixo, compara-se as medianas da notas de
    homens e mulheres de um colégio aleatório. Como a hipótese
    nula foi aceita, pode-se dizer que **não há uma diferença
    significante entre as medianas das notas de homens 
    e mulheres.**

        ![Evidência 18](./evidencias/curso_estatistica_para_analise_de_dados/sec06/teste_mann_whitney_n_parametrico.png) 

    - `Correlação:` O gráfico de dispersão mostra uma 
    relação entre as **notas finais e as notas de redação 
    de um grupo de alunos de um colégio aleatório**.A 
    distribuição dos pontos no gráfico indica uma 
    tendência geral de que quanto maior a nota na 
    redação, maior tende a ser a nota final. 
    Isso sugere que **a performance na redação tem um 
    impacto positivo na nota final do aluno**.

        ![Evidência 19](./evidencias/curso_estatistica_para_analise_de_dados/sec06/correlacao.png)

###  ➣ Curso: SQL para Análise de Dados: Do básico ao avançado 

- **Seção 3: Comandos básicos**<br>
    Na seção 3 do curso de SQL foi possível aprender os
    conceitos mais básicos, porém muito importantas 
    relacionados a linguagem SQL, como o `SELECT`, `FROM`,
    `WHERE`, `DISTINCT`, `ORDER BY` e `LIMIT`. Tais 
    conceitos permitem que consultas básicas até avançadas
    sejam realizadas.

    - Uso de comandos básicos em uma tabela de vendas

        ![Evidência 20](./evidencias/curso_sql_analise_de_dados/desafio_sec3.png)

- **Seção 4: Operadores**<br>
    A seção 4 aborda os **operadores aritméticos, de
    comparação e lógicos**. Esses operadores oferecem muitas
    possibilidades para a realização de consultas e que 
    mais insights possam ser obtidos.

    - Exercícios seção 4 que utilizam operadores como `BETWEEN` e `AND`.

        ![Evidência 21](./evidencias/curso_sql_analise_de_dados/desafio_sec4.png)

    - Exercícios que utilizam o operadores `LIKE` e `NOT`.

        ![Evidência 22](./evidencias/curso_sql_analise_de_dados/desafio_sec4_2.png)

- **Seção 5: Funções agregadas**<br>
    A seção 5 introduz as funções agregadas. Elas abrem um 
    leque grande de possibilidades para a compreensão e análise de 
    dados de uma tabela. Funções como `COUNT`, `MAX`, `MIN`,
    `GROUP BY`, `ORDER BY` e `HAVING` foram aprendidas.
    
    - Exercícios que utilizam funções agregadas para diferentes
    situações

        ![Evidência 23](./evidencias/curso_sql_analise_de_dados/desafio_sec5.png)

- **Seção 6: Joins**<br>
    Na seção 6 somos introduzidos aos tipos de `Joins` em
    SQL. Os principais e mais utilizados são o `INNER`, `LEFT`,
    `RIGHT` e `FULL`, usados para combinar dados de diferentes tabelas.

    - Exercícios utilizando `LEFT JOIN`

        ![Evidência 24](./evidencias/curso_sql_analise_de_dados/desafio_sec6.png)

- **Seção 8: Subqueries**<br>
    Na seção 8 vemos a introdução ao uso de `subqueries` para criar consultas aninhadas e flexíveis.

    - Exercício utilizando subquery

        ![Evidência 25](./evidencias/curso_sql_analise_de_dados/desafio_sec8.png)


- **Seção 9: Tratamento de dados**<br>
    Aprendizado sobre tratamento de dados, incluindo manipulação de datas com EXTRACT e ajustes gerais em tabelas.

    - Tratamento de datas utilizando `EXTRACT`

        ![Evidência 26](./evidencias/curso_sql_analise_de_dados/sec9_tratamento_datas_extract.png)

    - Tratamento geral

        ![Evidência 27](./evidencias/curso_sql_analise_de_dados/sec9_tratamento_geral.png)

- **Seção 10: Manipulação de tabelas**<br>
    Aprendizado sobre criação e deleção de tabelas, manipulação de colunas e inserção de dados.

    - Criação e deleção de colunas

        ![Evidência 28](./evidencias/curso_sql_analise_de_dados/sec10_criacao_e_delecao_tabelas.png)

    - Inserção de linhas

        ![Evidência 29](./evidencias/curso_sql_analise_de_dados/sec10_insercao_linhas.png)

# 👨🏼‍🎓 Certificados


- Certificado do Curso **Estatística para Análise de Dados com Python**

    ![Certificado](certificados/estatistica_para_analise_de_dados.jpg)

- Certificado do Curso **SQL para Análise de Dados: Do básico ao avançado**

    ![Certificado](certificados/sql_para_analise_de_dados.jpg)

