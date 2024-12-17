-- SEC 9

--Conversão de unidades
-- (Exemplo 1) Conversão de texto em data
-- Corrija a query abaixo utilizando o operador ::
SELECT '2021-10-01'::date - '2021-02-01'::date

SELECT nome_coluna::date
FROM nome_tabela


-- Tratamento Geral
-- (Exemplo 1) Agrupamento de dados com CASE WHEN
-- Calcule o nº de clientes que ganham abaixo de 5k, entre 5k e 10k, entre 10k e 
-- 15k e acima de 15k
WITH faixa_de_renda
AS (
	SELECT income
		,CASE 
			WHEN income < 5000
				THEN '0-5000'
			WHEN income >= 5000
				AND income < 10000
				THEN '5000-10000'
			WHEN income >= 10000
				AND income < 15000
				THEN '10000-15000'
			ELSE '15000+'
			END AS faixa_renda
	FROM sales.customers
	)
SELECT faixa_renda
	,count(*)
FROM faixa_de_renda
GROUP BY faixa_renda


-- Tratamento de texto
-- (Exemplo 1) Corrija o primeiro elemento das queries abaixo utilizando os comandos 
-- de tratamento de texto para que o resultado seja sempre TRUE 
SELECT 'São Paulo' = 'SÃO PAULO'

SELECT upper('São Paulo') = 'SÃO PAULO'

SELECT 'São Paulo' = 'são paulo'

SELECT lower('São Paulo') = 'são paulo'

SELECT 'SÃO PAULO     ' = 'SÃO PAULO'

SELECT trim('SÃO PAULO     ') = 'SÃO PAULO'

SELECT 'SAO PAULO' = 'SÃO PAULO'

SELECT replace('SAO PAULO', 'SAO', 'SÃO') = 'SÃO PAULO'



-- Tratamento de datas
-- (Exemplo 3) Extração de unidades de uma data utilizando EXTRACT
-- Calcule qual é o dia da semana que mais recebe visitas ao site
SELECT extract('dow' FROM visit_page_date) AS dia_da_semana
	,count(*)
FROM sales.funnel
GROUP BY dia_da_semana
ORDER BY dia_da_semana


-- Funções
-- (Exemplo 1) Crie uma função chamada DATEDIFF para calcular a diferença entre
-- duas datas em dias, semanas, meses, anos
SELECT (CURRENT_DATE - '2018-06-01')
SELECT (CURRENT_DATE - '2018-06-01') / 7
SELECT (CURRENT_DATE - '2018-06-01') / 30
SELECT (CURRENT_DATE - '2018-06-01') / 365
SELECT datediff('weeks', '2018-06-01', CURRENT_DATE)

CREATE FUNCTION datediff (
	unidade VARCHAR
	,data_inicial DATE
	,data_final DATE
	)
RETURNS INTEGER LANGUAGE sql
AS
$$

SELECT CASE 
		WHEN unidade IN (
				'd'
				,'day'
				,'days'
				)
			THEN (data_final - data_inicial)
		WHEN unidade IN (
				'w'
				,'week'
				,'weeks'
				)
			THEN (data_final - data_inicial) / 7
		WHEN unidade IN (
				'm'
				,'month'
				,'months'
				)
			THEN (data_final - data_inicial) / 30
		WHEN unidade IN (
				'y'
				,'year'
				,'years'
				)
			THEN (data_final - data_inicial) / 365
		END AS diferenca $$

SELECT datediff('years', '2021-02-04', CURRENT_DATE)

-- (Exemplo 2) Delete a função DATEDIFF criada no exercício anterior
DROP FUNCTION datediff