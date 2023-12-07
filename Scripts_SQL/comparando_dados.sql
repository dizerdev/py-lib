USE Clientes;

-- Comparação de campos que serão iguais nas 2 tabelas
SELECT nomeCliente FROM Clientes2016
INTERSECT
SELECT nomeCliente FROM Clientes2017;

-- Outra comparação de estar em uma e não estar em outra
SELECT nomeCliente FROM Clientes2016
INTERSECT
SELECT nomeCliente FROM Clientes2017;

-- Verificando se não existe dado entre 2 tabelas
SELECT nomeCliente FROM Clientes2016
EXCEPT
SELECT nomeCliente FROM Clientes2017;

SELECT nomeCliente FROM Clientes2017
EXCEPT
SELECT nomeCliente FROM Clientes2016; 