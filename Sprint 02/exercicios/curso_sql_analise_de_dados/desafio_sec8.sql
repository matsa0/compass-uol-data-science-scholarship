-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Crie uma coluna calculada com o número de visitas realizadas por cada
-- cliente da tabela sales.customers

WITH numero_visitas as (
	SELECT customer_id, count(*) as num
	FROM sales.funnel
	GROUP BY customer_id
)
SELECT cust.*n, num
FROM sales.customers as cust
LEFT JOIN numero_visitas
ON cust.customer_id = numero_visitas.customer_id