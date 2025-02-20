
<h1 align="center">
    <strong>SPRINT 07</strong>
</h1>

# 🔗 Vídeo - [Desafio Sprint 07]()


# 📝 Exercícios

## 🧠 Curso: Credit Risk Modeling in Python

### Section 1: Introduction

### Section 2: Setting up the working enviroment

### Section 3: Dataset description

### Section 4: General preprocessing

### Section 5: PD model: Data Preparation

### Section 6: PD model estimation

### Section 7: PD model validation

### Section 8: Applying the PD model for decision making

### Section 9: PD model monitoring

### Section 10: LGD and EAD models: Preparing the data

### Section 11: LGD model

### Section 12: EAD model

### Section 13: Calculating expected loss


## 🧠 Curso: Amazon Bedrock, Amazon Q & AWS Generative AI

### Section 2: Basics of AI, ML & Neural Networks

### Section 3: Generative AI & Foundation Models Concepts

### Section 4: Amazon Bedrock - Deep Dive

### Section 5: Enterprise Use Case 1: Image Generation 

### Section 6: Enterprise Use Case 2: Text Summarization

### Section 7: Use Case 3: Building a Chatbot

### Section 8: Overview of Vectors & Embeddings

### Section 9: Use Case 4: Building HR Q&A




# 🔎 Evidências

## 🧠 Curso: Credit Risk Modeling in Python

### Section 1: Introduction

### Section 2: Setting up the working enviroment

### Section 3: Dataset description

### Section 4: General preprocessing

### Section 5: PD model: Data Preparation

### Section 6: PD model estimation

### Section 7: PD model validation

### Section 8: Applying the PD model for decision making

### Section 9: PD model monitoring

### Section 10: LGD and EAD models: Preparing the data

### Section 11: LGD model

### Section 12: EAD model

### Section 13: Calculating expected loss



## 🧠 Curso: Amazon Bedrock, Amazon Q & AWS Generative AI

### Section 2: Basics of AI, ML & Neural Networks
A seção 2 foi interessante de ser realizada para a recordação de importantes conceitos que vemos durante a trilha relacionados Inteligência Artificial(AI), Machine Learning(ML), Deep Learning(DL) e Generative AI.

- **Aprendizado supervisionado**: modelos são treinados utilizando **datasets rotulados**. O objetivo é que o modelo aprenda a mapear as entradas para as saídas corretas e consiga fazer previsões para novos dados. Esse tipo de aprendizado é utilizando para resolver problemas de **classificação** e **regressão**.

- **Aprendizado não supervisionado**: o algoritmo é treinado utilizando **datasets não rotulados**. Baseado no conjunto de dados, o modelo consegue encontrar padrões escondidos e insights baseados nas similaridades dos dados. Esse tipo de aprendizado é muito utilizado em problemas de **clusterização** e **redução de dimensionalidade**.

- **Deep Learning**: subárea de Machine Learning que utiliza redes neurais profundas para **aprender representações complexas dos dados**. O treinamento dessas redes exige grandes volumes de dados e alto poder computacional. Muito utilizado para **reconhecimento de imagens** e **processamento de linguagem natural**.

- **IA Generativa**: subárea de Deep Learning que foca em criar modelos capazes de **gerar conteúdo** a partir de padrões aprendidos. Por exemplo, pode-se ter IA's generativas baseadas em texto, imagens, vídeos, aúdios, código, entre outros. ChatGPT, DeepSeek, MidJourney são exemplos de IA's generativas.

### Section 3: Generative AI & Foundation Models Concepts
Nesta seção 3, a gente vai um pouco mais fundo no conceito de IA Generativa.

Utilizando o **Chat/Text playground** do `Claude 3 Haiku`, eu perguntei "O que é uma IA Generativa?", e ela me retornou a seguinte resposta:

![Evidencia](./evidencias/curso_amazon_bedrock/sec3/ia_generativa.png)

Uma IA Generativa funciona através de um `modelo fundamental`, que é o modelo treinado com um grande conjunto de dados para capturar padrões gerais. 

A IA é utilizada através de um `prompt`, que significa a entrada do usuário, podendo ser um texto, uma imagem, vídeo ou aúdio, contendo uma instrução do usuário para a IA.

O processamento do prompt fornecido pelo usuário é realizado pela IA para analisar o prompt e prever uma melhor resposta com base no que aprendeu no treinamento. Esse proceso é chamado de `inferência`, e a resposta gerada, é chamada de `completion`.

Após receber um prompt, a IA realiza o proceso de `tokenização`, que transforma o prompt em tokens numéricos, além disso, ela deve levar em conta a janela de contexto(`context window`), que define quantos tokens o modelo pode levar em consideração para dar uma resposta. O `detokenizer` reconverte os tokens para palavras, para gerar o completion.

É importante compreender 3 conceitos de modelos fundamentais.

- **Tokens**: um token geralmente corresponde a 4 caracteres de texto.
- **Parameters**- númeo de conexões e pesos entre nós em uma rede neural.
- **Temperature** - parâmetro que controla a criatividade e diversidade do modelo.

Exemplo de resposta do modelo `Llama` da Meta para o prompt *"Qual é o melhor jogador de todos os tempos?"*, com parâmetros como **Temperature** e **Top P** ajustados.

![Evidencia](./evidencias/curso_amazon_bedrock/sec3/chat_llama.png)

Outro caso de uso de IA Generativa, é a **geração de imagens**, como no exemplo abaixo, onde utilizei o modelo `Titan Image Generator` da Amazon e coloquei um o prompt: *"Um gato fazendo exercícios na academia"*. A IA me retornou a imagem abaixo:

![Evidencia](./evidencias/curso_amazon_bedrock/sec3/Um%20gato%20fazendo%20exercícios%20na%20academia.png)

### Section 4: Amazon Bedrock - Deep Dive
Na seção 4, os conceitos da ferramenta Amazon Bedrock são mais aprofundados, assim como a sua utilização.

Amazon Bedrock é um serviço totalmente gerenciado pela AWS e servless, ou seja, você é cobrado apenas pelo que usa. Existem vários modelos fundamentais que estão disponíveis no Bedrock, mas nessa sprint, trabalhei apenas com o `Llama` da Meta, `Claude 3 Haiku` da Anthropic e o `Titan Image Generator G1` da Amazon.

É possível fazer uma customização de modelos através do **fine-tuning**, onde você pode ajuste um modelo de IA para tarefas específicas usando um conjunto de dados rotulado.

A arquitetura do AWS Bedrock segue o seguinte fluxo: Solicitação do cliente -> Processamento no AWS Bedrock -> Chamada ao provedor de modelos -> Acesso ao modelo base(fundamental).

Três principais componentes:
- **Runtime Inference**: Determina para qual endpoint o pedido será enviado.
- **Base Model**: Modelos pré-treinados disponíveis para os clientes.
- **Bedrock Service**: Camada gerenciada da AWS que conecta os clientes aos modelos de IA.

Os parâmetros de inferência influenciam diretamente na forma como os modelos de IA Generativa irão gerar as respostas. Abaixo, os principais parâmetros para cada categoria são descritos:

**1. Randomness and Diversity**
- **Temperature**: Controla a aleatoriedade na escolha das palavras. Valores mais altos resultam em respostas mais criativas e imprevisíveis.

- **Top K**: Define um limite para a quantidade de palavras candidatas para cada próxima palavra gerada.

- **Top P**: Usa um critério de probabilidade cumulativa para limitar as escolhas de palavras.

**2. Length**
- **Response Length**: Determina o número máximo de tokens (palavras ou partes de palavras) gerados.

- **Length Penalty**: Penaliza respostas muito curtas ou muito longas para equilibrar a saída.

- **Stop Sequence**: Define uma sequência específica que faz o modelo parar de gerar texto quando encontrada.

**3. Repetition**
- **Repetition Penalty**: Reduz a probabilidade de repetir palavras ou frases.

### Section 5: Enterprise Use Case 1: Image Generation 
Na seção 5 estudamos um caso de uso de IA Generativa com o objetivo de **gerar um design de um cartaz de um fime**.

O fluxo utilizado para trabalhar com a IA Generativa é descrito abaixo:

O Usuário vai utilizar uma API Rest para **realizar um prompt** para um `API Gateway`, que vai gerar um evento para uma função do `AWS Lambda` que vai encaminhar o **prompt + os parâmetros de inferência** para o `AWS Bedrock`. O Bedrock vai interagir com a IA Generativa que vai **gerar a imagem**, e ele também vai armazená-la em um `bucket S3`.

O passo-a-passo para implementação da arquitetura é o seguinte:

1. Criação do bucket
2. Criação da função AWS Lambda
3. Criação de uma API Rest usando o AWS API Gateway
4. Testar utilizando alguma ferramenta de requisição

Após criar o bucket s3, criei uma função AWS Lambda com o objetivo de com um prompt de geração de imagem, realizar uma requisição para o modelo `Titan Image Generator G1`, retornar uma imagem e armazenar no bucket s3 criado.

![Evidencia](./evidencias/curso_amazon_bedrock/sec5/promptTest.png)

Acima, o prompt fornecido por Test que eu estava rodando era **"image of two cats"**.

![Evidencia](./evidencias/curso_amazon_bedrock/sec5/request.png)

As configurações da requisição são as acima, onde com a documentação referente ao modelo utilizado, é possível saber o que colocar no **corpo da requisição** e ajustar os **parâmetros de inferência** como número de imagens, tamanho, qualidade, entre outros.

Após mais alguns processos como decodificar a imagem gerado em base64, uma integração com o bucket s3 foi feita, ela foi armazenada nele.

![Evidencia](./evidencias/curso_amazon_bedrock/sec5/armazenando_bucket.png)

A imagem gerada:

![Evidencia](./evidencias/curso_amazon_bedrock/sec5/image_of_2_cats.png)

Nesta seção também foi criado uma API no serviço `AWS API Gateway`, onde é possível realizar requisições GET através do **Invoke URL**, passando o prompt como parâmetro. Dentro do serviço API Gateway, é possível realizar um teste e ver a response. 

![Evidencia](./evidencias/curso_amazon_bedrock/sec5/request_api.png)

Coloquei o prompt "a sunny day in a beautiful landscape" e obtive a seguinte imagem:

![Evidencia](./evidencias/curso_amazon_bedrock/sec5/beautiful_landscape.png)

### Section 6: Enterprise Use Case 2: Text Summarization
Na seção 6, o caso de uso trabalhado, é a utilização de **sumarização de texto** com AWS Bedrock para resolução de problemas mais rapidamente. Em um cenário real, esse caso de uso aumentaria a produtividade de técnicos em uma indústria de manufatura.

Em caso de mal funcionamento ou problemas em algum equipamento em um lugar remoto, técnicos serão acionados para visitar o local. Após realizar a vistoria, ele iria **reportar o incidente**. As evidências serão enviadas para uma aplicação feita para receber esse reporte, podendo ser textos ou imagens. Essa aplicação irá encaminhar o incidente para um modelo base no AWS Bedrock e retornar um **reporte sumarizado e organizado**.

O primeiro passo é construir uma comunicação com o AWS Bedrock. O modelo invocado para a realização da tarefa foi o `Claude 3 Haiku`. 

![Evidencia](./evidencias/curso_amazon_bedrock/sec6/codigo_invocando_claude.png)

Acima é possível observar que um prompt é passado no campo messages. Esse prompt foi definido no evento de teste como uma pergunta **"What are you?"**, para fins de teste. A seguinte resposta foi retornada pelo Claude.

![Evidencia](./evidencias/curso_amazon_bedrock/sec6/response_claude.png)

Outro passo muito importante foi a criação da API através do API Gateway. Após criar o método POST e realizar um deploy, a API ficou disponível para utilização. Realizei um teste na ferramenta Insomnia através do Invoke URL, passando no body, um prompt que contém um **exemplo de reporte que pode ter sido realizado por um técnico** e pedi para sumarizá-lo em 2 linhas.

A Request:
![Evidencia](./evidencias/curso_amazon_bedrock/sec6/request_insomnia.png)

A Response:
![Evidencia](./evidencias/curso_amazon_bedrock/sec6/response_insomnia.png)


### Section 7: Use Case 3: Building a Chatbot
Nesta seção contruímos um **Chatbot** utilizando ferramentas como `Stramlit` + `Langchain` + `Bedrock`.

Para fins de contexto, **Streamlit** é uma biblioteca em Python que facilita a criação de **interfaces web interativas**. **Langchain** também é uma biblioteca, e facilita a construção de **aplicações que são baseads em LLMs**.

O fluxo da arquitetura pode ser representado da seguinte maneira:

- O usuário **interage com o chatbot** através da interface do Streamlit
- O chatbot usa a **Langchain Memory** para recuperar mensagens anteriores e manter o **contexto da conversa**
- O Langchain combina a **pergunta atual** com o **histórico de conversa** para formar um prompt mais completo
- O prompt é enviado para um modelo de IA na Amazon Bedrock, que **processa a pergunta e gera uma resposta**
- A resposta gerada pelo modelo da Amazon Bedrock é **processada e formatada** para garantir que esteja correta.
- A **resposta é exibida** na interface do Streamlit, completando o ciclo de interação.

Através das credenciais de acesso da AWS no ambiente de trabalho, foi possível utilizar modelos fundamentais como o Claude 3 Haiku para construir o chatbot.

![Evidencia](./evidencias/curso_amazon_bedrock/sec7/claude3_haiku.png)

Passei o prompt "Hi, what is your name?" como input e rodei o código e obtive a seguinte resposta:

![Evidencia](./evidencias/curso_amazon_bedrock/sec7/response_claude3.png)

O modelo já estava provendo respostas, portanto, foi preciso realizar mais algumas configurações como o buffer de conversas para questões como a memória e histórico sejam exploradas.

![Evidencia](./evidencias/curso_amazon_bedrock/sec7/erro_frontend.png)

Infelizmente não consegui explorar muito a utilziação da interface por conta de um erro que não consegui resolução.

### Section 8: Overview of Vectors & Embeddings
A seção 8 foi muito interessante para relembrar conceitos fundamentais de machine learning e processamento de linguagem natural(NLP) como os **vetores** e **embeddings**.

Os embeddings são representações vetoriais densas de dados textuais. Eles transformam texto em **vetores numéricos** que capturam o significado semântico das palavras, frases ou documentos. 

Nesta seção desenvolvemos um código onde utilizamos o modelo fundamental `Amazon Titan Embedding Text v2` para gerar um **embedding como resposta para um prompt passado**. Nesse contexto, eu passei o input: "Hi! My name is Matheus. How are you?". Esse texto foi enviado ao modelo, que processa o texto e gera um emebdding.

Através do CloudWatch, vemos o Log gerado com as informações impressas.

![Evidencia](./evidencias/curso_amazon_bedrock/sec8/log_cloud_watch_embedding.png)

Acima é possível ver o prompt passado em conjunto com seu número de tokens gerados, o total de embeddings gerados e o vetor denso que representa o texto de resposta.   


### Section 9: Use Case 4: Building HR Q&A
Na seção 9 nós trabalhamos com o HR Q&A com RAG, que é um sistema de **perguntas e respostas(Q&A)** voltado para **recursos humanos(HR)**, utilizando a técnica de **geração aumentada por recuperação(RAG)** para melhorar a precisão das respostas fornecidas por um modelo de inteligência artificial.

**Retrieval-Augmented Generation(RAG)** é um conceito novo que é importante de ser entendido. RAG é uma abordagem de inteligência artificial generativa que busca melhorar a precisão das respostas. Isso é algo importante, pois modelos de IA generativa podem **inventar respostas**, conhecido como alucinações, ou gerá-las com base a**penas nos dados que aprendeu durante o treinamento**. 

Com o RAG, um sistema busca informações relevantes em um **banco de dados** ou **corpus de documentos** (ex.: PDFs, sites, bases de conhecimento).  O modelo de linguagem recebe tanto a pergunta do usuário quanto o contexto recuperado.

Com o contexto acima, o sistema de perguntas e respostas voltado para recursos humanos foi criado.

O código implementa uma interface funcional para:

- Carregar e processar documentos PDF.
- Dividir o texto em chunks menores.
- Criar embeddings para os chunks de texto.
- Armazenar os embeddings em um banco de dados vetorial.
- Configurar e usar um modelo de linguagem para responder a perguntas com base nos dados processados.

![Evidencia](./evidencias/curso_amazon_bedrock/sec9/hr_QA_interface.png)

Acima, tem-se um exemplo de uso, onde o prompt passado foi **"how many time leave for maternity?"**.

# 👨🏼‍🎓 Certificados

## 🧠 Curso: Credit Risk Modeling in Python


## 🧠 Curso: Amazon Bedrock, Amazon Q & AWS Generative AI

