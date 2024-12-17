-- SEC 10

-- Tabelas - Criação e deleção
-- (Exemplo 2) Criação de tabela a partir do zero
-- Crie uma tabela com a tradução dos status profissionais dos clientes. 
-- Chame-a de temp_tables.profissoes
SELECT DISTINCT professional_status
FROM sales.customers

CREATE TABLE temp_tables.profissoes (
	professional_status VARCHAR
	,status_profissional VARCHAR
	)

INSERT INTO temp_tables.profissoes (
	professional_status
	,status_profissional
	)
VALUES ('freelancer','freelancer'),
('retired','aposentado(a)'),
('clt','clt'),
('self_employed','autônomo(a)'),
('other','outro'),
('businessman','empresário(a)'),
('civil_servant','funcionário público(a)'),
('student','estudante')

SELECT *
FROM temp_tables.profissoes

-- (Exemplo 3) Deleção de tabelas
-- Delete a tabela temp_tables.profissoes
DROP TABLE temp_tables.profissoes


-- Linhas
-- (Exemplo 1) Inserção de linhas
-- Insira os status 'desempregado(a)' e 'estagiário(a)' na temp_table.profissoes
CREATE TABLE temp_tables.profissoes (
	professional_status VARCHAR
	,status_profissional VARCHAR
	);

INSERT INTO temp_tables.profissoes (
	professional_status
	,status_profissional
	)
VALUES ('freelancer','freelancer'),
('retired','aposentado(a)'),
('clt','clt'),
('self_employed','autônomo(a)'),
('other','outro'),
('businessman','empresário(a)'),
('civil_servant','funcionário público(a)'),
('student','estudante')

SELECT *
FROM temp_tables.profissoes

INSERT INTO temp_tables.profissoes (
	professional_status
	,status_profissional
	)
VALUES (
	'unemployed'
	,'desempregado(a)'
	)
	,(
	'trainee'
	,'estagiario(a)'
	)

-- (Exemplo 2) Atualização de linhas
-- Corrija a tradução de 'estagiário(a)' de 'trainee' para 'intern' 
UPDATE temp_tables.profissoes
SET professional_status = 'intern'
WHERE status_profissional = 'estagiario(a)'

SELECT *
FROM temp_tables.profissoes

-- (Exemplo 3) Deleção de linhas
-- Delete as linhas dos status 'desempregado(a)' e 'estagiário(a)'
DELETE
FROM temp_tables.profissoes
WHERE status_profissional = 'desempregado(a)'
	OR status_profissional = 'estagiario(a)'

SELECT *
FROM temp_tables.profissoes