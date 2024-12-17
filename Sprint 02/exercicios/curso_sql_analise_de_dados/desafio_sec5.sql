-- (Exercício 1) Conte quantos clientes da tabela sales.customers tem menos de 30 anos
SELECT count(*)
FROM sales.customers
WHERE birth_date > '1994-12-10'

-- (Exercício 2) Informe a idade do cliente mais velho e mais novo da tabela sales.customers
SELECT max((CURRENT_DATE - birth_date) / 365) AS mais_velho
	,min((CURRENT_DATE - birth_date) / 365) AS mais_novo
FROM sales.customers

-- (Exercício 3) Selecione todas as informações do cliente mais rico da tabela sales.customers
-- (possívelmente a resposta contém mais de um cliente)
SELECT *
FROM sales.customers
WHERE income = (
		SELECT max(income)
		FROM sales.customers
		)

-- (Exercício 4) Conte quantos veículos de cada marca tem registrado na tabela sales.products
-- Ordene o resultado pelo nome da marca
SELECT brand
	,count(brand)
FROM sales.products
GROUP BY brand
ORDER BY brand

-- (Exercício 5) Conte quantos veículos existem registrados na tabela sales.products
-- por marca e ano do modelo. Ordene pela nome da marca e pelo ano do veículo
SELECT brand
	,model_year
	,count(*)
FROM sales.products
GROUP BY brand
	,model_year
ORDER BY brand
	,model_year

-- (Exercício 6) Conte quantos veículos de cada marca tem registrado na tabela sales.products
-- e mostre apenas as marcas que contém mais de 10 veículos registrados
SELECT brand
	,count(*)
FROM sales.products
GROUP BY brand
HAVING count(*) > 10
ORDER BY count(*) ASC
