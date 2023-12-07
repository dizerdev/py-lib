USE Clientes;

SELECT * FROM Clientes2016
UNION
SELECT * FROM Clientes2017;

-- Selecionando a ordem por numero
SELECT * FROM Clientes2016
UNION
SELECT * FROM Clientes2017
ORDER BY 2 ASC;

-- ou o nome da coluna
SELECT * FROM Clientes2016
UNION
SELECT * FROM Clientes2017
ORDER BY nomeCliente DESC;

-- Usando uma coluna virtual na consulta
-- O nome da coluna é somente no primeiro select
SELECT 'Clientes 2016' AS 'Ano','Aprovados' AS 'Situação',* FROM Clientes2016
WHERE nomeCidade = 'SÃO PAULO' AND nomeCidade = 'SANTOS'
UNION
SELECT 'Clientes 2017','Aprovados',* FROM Clientes2017
WHERE nomeCidade = 'SÃO PAULO' 
	OR nomeCidade = 'SANTOS' 
	OR NOT valorApolice <= 30000
ORDER BY 4 ASC;

-- UNION ALL
SELECT * FROM Clientes2016
UNION ALL
SELECT * FROM Clientes2017
ORDER BY 2 ASC;

UPDATE Clientes2016
SET valorApolice = 30000
WHERE idCliente = 2810;