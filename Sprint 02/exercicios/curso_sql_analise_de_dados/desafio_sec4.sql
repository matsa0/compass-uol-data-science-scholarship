-- EXERCÍCIOS 

-- (Exercício 1) Calcule quantos salários mínimos ganha cada cliente da tabela 
-- sales.customers. Selecione as colunas de: email, income e a coluna calculada "salários mínimos"
-- Considere o salário mínimo igual à R$1200

select first_name, last_name, email, income, 
	round((income / 1200), 2) as min_wages
from sales.customers;


-- (Exercício 2) Na query anterior acrescente uma coluna informando TRUE se o cliente
-- ganha acima de 5 salários mínimos e FALSE se ganha 4 salários ou menos.
-- Chame a nova coluna de "acima de 4 salários"

select first_name, last_name, email, income,
	round((income / 1200), 2) as min_wages,
	((income / 1200) >= 5) as more_than_five_wages
from sales.customers;


-- (Exercício 3) Na query anterior filtre apenas os clientes que ganham entre
-- 4 e 5 salários mínimos. Utilize o comando BETWEEN

select first_name, last_name, email, income
FROM sales.customers
where (income / 1200) BETWEEN 4 and 5

-- (Exercício 4) Selecine o email, cidade e estado dos clientes que moram no estado de 
-- Minas Gerais e Mato Grosso. 

select email, city, state
from sales.customers
where state BETWEEN 'MG' and 'MT'

-- (Exercício 5) Selecine o email, cidade e estado dos clientes que não 
-- moram no estado de São Paulo.


select email, city, state
from sales.customers
where NOT state = 'SP'

-- (Exercício 6) Selecine os nomes das cidade que começam com a letra Z.
-- Dados da tabela temp_table.regions

select city
from temp_tables.regions
where city like 'Z%'