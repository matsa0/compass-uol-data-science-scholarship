-- EXERCÍCIOS 

-- (Exercício 1) Identifique quais as marcas de veículo mais visitada na tabela sales.funnel
SELECT * FROM sales.funnel

SELECT pro.brand, count(*) as visitas
FROM sales.products as pro
LEFT JOIN sales.funnel as fun
	ON fun.product_id = pro.product_id
GROUP BY pro.brand
ORDER BY visitas DESC

-- (Exercício 2) Identifique quais as lojas de veículo mais visitadas na tabela sales.funnel
SELECT * FROM sales.stores

SELECT sto.store_name, COUNT(*) as visitas
FROM sales.funnel as fun
LEFT JOIN sales.stores as sto
	ON fun.store_id = sto.store_id
GROUP BY sto.store_name
ORDER BY visitas DESC


-- (Exercício 3) Identifique quantos clientes moram em cada tamanho de cidade (o porte da cidade
-- consta na coluna "size" da tabela temp_tables.regions)

SELECT * FROM temp_tables.regions

SELECT * FROM sales.customers

SELECT rg.size, count(*) as qnt
FROM sales.customers as cus
LEFT JOIN temp_tables.regions as rg
	ON lower(cus.city) = lower(rg.city) AND
	lower(cus.state) = lower(rg.state)
GROUP BY rg.size
ORDER BY qnt