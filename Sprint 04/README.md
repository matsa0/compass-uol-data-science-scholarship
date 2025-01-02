
<h1 align="center">
    <strong>SPRINT 03</strong>
</h1>

# 📝 Exercícios

No diretório de exercícios, coloquei alguns noteboooks que eu trabalhei durante o curso.

# 🔴 Vídeo - [Desafio Sprint 04]

# 🔎 Evidências

### ➣ Curso: Machine Learning com Amazon AWS e SageMaker

### ➣ Curso: Machine Learning e Data Science com Python de A a Z

- **Seção 14: Regressão Linear**<br> A regressão linear é um conceito estatístico que busca realizar a modelagem da relação entre variáveis numéricas, sendo separadas em uma `variável dependente(alvo)` e `variáveis independentes(preditores)`. O principal objetivo é encontrar a **melhor linha reta** que mostre a relação entre essas variáveis e dizer o quão bem a variável dependente pode ser **prevista** pelas variáveis preditoras.

    - **Regressão Linear Simples:** esse tipo de regressão linear relaciona uma variável dependendete a uma única variável independente.

        ![Evidencia](./evidencias/sec14/regressao_linear_simples.png)

    Prever o custo de um plano de saúde baseado na idade de uma pessoa. O modelo foi criado tendo como variável dependente(y) o `custo` e independente(X) `idade`.

    A linha vermelha representa as previsões realizadas pelo modelo.

    - **Regressão Linear Múltipla:** esse tipo de regressão linear relaciona uma variável dependendete a múltiplas variáveis independentes.

        Selecionando as variáveis independentes e a dependente(`price`). A ideia é prever o preço de uma casa com base em diversas outras variáveis.

        ![Evidencia](./evidencias/sec14/regressao_multipla_variaveis.png)

        Previsões e `Mean Absolute Error`

        ![Evidencia](./evidencias/sec14/regressao_multipla.png)

- **Seção 15: Outros tipos de regressão**<br>

    - **Regressão Polinomial:**<br> Uma extensão da regressão linear que permite capturar relações **não lineares** entre as variáveis. Útil quando a relação entre as variáveis não é linear e pode ser aproximada por uma **curva**.

        O parâmetro `degree = 4`permite que o modelo se ajuste bem, mas em outros cenários pode gerar overfitting em dados mais ruidosos.

        ![Evidencia](./evidencias/sec15/regressao_polinomial.png)

        ![Evidencia](./evidencias/sec15/regressao_polinomial2.png)

    - **Regressão com Random Forest**<br> O `Random Forest` faz parte do que se chama `Aprendizado em Conjunto(Ensemble Learning)`, que basicamente significa consultar diversas fontes para se obter um resultado mais preciso e robusto. O Random Forest utiliza de várias `árvores de decisão` para construir um algoritmo mais "forte". Além disso, utiliza a média(regressão) ou votos da maioria(classificação) para se obter uma resposta final.

        ![Evidencia](./evidencias/sec15/random_forest.png)

        A linha vermelha, que são os `degraus` passam próximas aos pontos reais, indicando que o modelo conseguiu capturar bem as variações presentes nos dados.

    - **Regressão com Redes Neurais Artificiais**<br> As RNAs são amplamente utilizadas para resolver problemas complexos, nesse caso, a regressão. Os dados de entrada (X) são escalados para melhorar o desempenho do treinamento, eles percorrem cada camada da rede realizando os cálculos de erros e ajuste de pesos.

        ![Evidencia](./evidencias/sec15/regressao_rna.png)

        O modelo parece ter se ajustado bem aos dados reais, dado que a linha vermelha segue o padrão dos pontos azuis.

- **Seção 17: Algoritmo Apriori**<br> Antes de explicar o algoritmo Apriori, é importante falar sobre as **regras de associação**.

    - **Regras de associação:**<br> As regras de associação tem como objetivo identificar **padrões e associações** entre conjunto de dados. Com esse conjunto de regras, é possível encontrar relações ocultas entre variáveis que geralmente não são esperadas.

    - É possível obter muitos **insights** que podem ser determinísticos para **tomadas de decisõe**s. Por exemplo, responder as seguintes perguntas:

        - Em que prateleira o biscoito de chocolate deve ser colocado para maximizar suas vendas?

        - Suco de uva costuma ser comprado com refrigerante?

        - Qual produto deve ser colocado em promoção para uma venda casada com tomates?

    - **Apriori:**<br> O `Apriori` busca encontrar conjuntos frequentes de itens em transações e derivar regras de associação que indicam relações entre os itens.

    - 3 conceitos são fundamentais de saber ao se estudar regras de associação e Apriori:

        `Suporte (Support):` Frequência com que um conjunto de itens aparece nas transações.

        `Confiança (Confidence):` Probabilidade de que, se um item AA é comprado, BB também seja.

        `Lift:` Mede a força da regra. Um valor maior que 1 indica uma associação positiva entre AA e BB.

        No Apriori, apenas os conjuntos de itens que **atendem ao suporte mínimo definido** pelo usuário são mantidos. Além disso, a partir desse conjunto de itens mantidos, o objetivo é descobrir regras de associação com fator de **confiança maior ou igual** ao estabelecido pelo usuário.
 

- **Seção 20: Agrupamento com K-Means**<br>

- **Seção 21: Outros algoritmos de agrupamento**<br>

- **Seção 27: Seleção de atributos**<br>

- **Seção 28: Redução de dimensionalidade**<br>

- **Seção 29: Detecção de Outliers**<br>


# 👨🏼‍🎓 Certificados

- Certificado do Curso **Machine Learning com Amazon AWS e SageMaker**

- Certificado do Curso **Machine Learning e Data Science com Python de A a Z**

