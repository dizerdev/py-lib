USE Clientes;

-- Compara��o de campos que ser�o iguais nas 2 tabelas
SELECT nomeCliente FROM Clientes2016
INTERSECT
SELECT nomeCliente FROM Clientes2017;

-- Outra compara��o de estar em uma e n�o estar em outra
SELECT nomeCliente FROM Clientes2016
INTERSECT
SELECT nomeCliente FROM Clientes2017;

-- Verificando se n�o existe dado entre 2 tabelas
SELECT nomeCliente FROM Clientes2016
EXCEPT
SELECT nomeCliente FROM Clientes2017;

SELECT nomeCliente FROM Clientes2017
EXCEPT
SELECT nomeCliente FROM Clientes2016; 