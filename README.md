# Rossmann Sales
![alt text]( https://github.com/OscarFantozzi/rossmann_sales/blob/main/img/rossmann.jpg)

## Business Problem
Rossmann é uma grande cadeia de farmácias que atua em mais de 7 países europeus com mais de 3000 lojas. As vendas são influenciadas por vários fatores como: distância do competidor, feriados escolares e estaduais, localidade, tipo de loja etc.Com base nos dados históricos de vendas das lojas o CFO pretende fazer uma previsão de venda para as próximas 6 semanas.Para solucionar o problema, vou tratar os dados e treinar um modelo de ML ( Machine Learning ) que consiga fazer uma previsão para as próximas 6 semanas com base no número da loja que for passado pra ele.

## Origem dos dados:
Para este estudo de caso, os dados foram retirados do site Kaggle. O Kaggle é um renomado site onde várias empresas promovem competições disponibilizando seus dados de maneira pública e premiando as equipes que trouxerem as melhores soluções.Abaixo disponibizo o link de onde os dados foram retirados, lembrando que os mesmos também se encontram na pasta "data" do github.

https://www.kaggle.com/competitions/rossmann-store-sales/data

## Ferramentas Utilizadas:
* Linguagem de programação: Python

## Método e resolução do problema
Para resolver este problema utilizei o método cíclico. O método cíclico 
é um método iterativo composto de várias etapas que são repetidas e melhoradas a cada iteração para gradualmente melhorarem a resolução do problema. O método cíclico prioriza uma entrega rápida, e após cada cíclo permite ir melhorando os resultados e as métricas do modelo de ML por exemplo.
As etapas para resolver o problema foram as seguintes:
* 1.0 - Descrição dos Dados
* 2.0 - Feature Engineering
* 3.0 - Filtragem de variáveis
* 4.0 - Análise Exploratória de Dados
* 5.0 - Data Preparation
* 6.0 - Feature Selection
* 7.0 - Machine Learning Modelling
* 8.0 - Hyperparameters Fine Tuning
* 9.0 - Tradução e Interpretação do Erro
* 10  - Deploy

Mais abaixo entrarei em detalhes sobre cada etapa acima.

## ETAPA 1: Descrição dos Dados
Em um dataset tabular ( dados em formato de tabela ), cada coluna representa um fenômeno e cada linha uma informação a respeito do fenômeno, sendo assim é importanto que as colunas tenham nomes intuitivos para facilitar o entendimento a respeito do que cada observação quer nos dizer. O dataset da Rossmann tem as seguintes colunas, que a partir de agora chamarei de features.

* store - identificado único da loja
  
* day_of_week - dia da semana em números inteiros

* date - data que foi feita a venda

* sales - valor das vendas em determinado dia

* customers - número de clientes em determinado dia

* open - indicador se a loja estava aberta e fechada 0 = closed, 1 = open

* promo - Indica se a loja estava com promoção naquele dia

* state_holiday - Indica se foi feriado estadual. Geralmente as lojas fecham nos feriados estaduais. Contém: a = public holiday, b = Easter holiday, c = Christmas, 0 = None

* school_holiday - Indica se a loja foi afeatada pelo fechamento de feriados escolares naquele dia.

* store_type - tipo de lojas, podem ser do tipo: a, b, c, d

* assortment - descrve o tipo de sortimento da loja: a = basic, b = extra, c = extended

* competition_distance - distância em metros do competidor mais próximo.

* competition_open_since_month - mostra o mês em que o competidor mais próximo foi aberto.

* competition_open_since_year - mostra o ano em que o competidor mais próximo foi aberto.

* promo2 - mostra se a loja teve uma extensão de promoção naquele dia da venda. Contém :  0 = store is not participating, 1 = store is participating

* promo2_since_week - a semana em que a loja esteve participando da promo2

* promo2_since_year - o ano que a loja esteve participando da promo2.

* promo_interval - mostra os meses consecutivos em que a loja teve promo2. Por exemplo: "Feb,May,Aug,Nov" significa que a loja participou da promo2 nos meses de Fevereiro, Maio, Agosto e Novembro daquele ano.


## ETAPA 2: Feature Engineering

A etapa de feature engineering consiste em criar novas features ( colunas ) a partir do dataset original, ou combinadas com outro dataset. É bastante comum por exemplo extrairmos as features "Ano", "Mês", "Dia" através de uma data no formato 'aaaa-mm-dd' para realizarmos análises com menores granularidades ou para construir tabelas agrupadas por Ano/Mês/Dia.

Abaixo algumas features que podem ser extraídas do dataset original ou combinando com outras fontes de dados.

![alt text]( https://github.com/OscarFantozzi/rossmann_sales/blob/main/img/img_hypothesis.jpg)

Nesse projeto foram extraídas as features temporais e ajustadas algumas features categóricas ( colunas que contém dados do tipo texto ). Também nesta etapa foram levantadas algumas hipóteses que irei validar com os dados e análises ( mais detalhes no notebook rossmann_sales.ipynb ).

## ETAPE 3: Filtragem de variáveis

Nesta etapa preparo o formato do dataset com as colunas e linhas que utilizarei para treinar modelo de ML. Basicamente consiste em filtras excluir linhas e colunas não relevantes no momento da predição. 
Nas linhas deixei somente as lojas que estão abertas e removi a feature 'customers' e outras features derivadas. O porquê da remoção da feature 'customers'( como informado acima, indica o número de clientes dentro da loja naquele dia ) se dá porquê no momento da predição, não consigo informar quantos clientes tenho naquela loja. 

## Análise Exploratória de Dados

Nesta etapa de análise exploratória de dados, análisei os dados atráves de análise univariada, bivariada e multivariada.

### Análise Univariada

Na análise univariada meu interesse vou ver a distribuição das features do dataset e suas características sem levar em consideração outras variáveis correlacionadas. Importante pois nos ajuda a responder perguntas quais: qual o valor médio da feature? Quais os valores mínimos e máximos? Que tipo de distribuição encontro na feature? Existem outliers?

### Análise Bivariada

Ná análise bivariada, meu interesse foi ver se existia alguma entre as features e a variável resposta. A variável resposta, é a feature que eu quero prever, no meu caso como quero prever as vendas das próximas 06 semanas, foi a feature "sales".Para verificar as correlações, levantei algumas hipóteses e tentei respondê-las combinando features. A análise bivariada me ajudou a perceber como uma feature se comporta em relação a variável resposta. 

### 
