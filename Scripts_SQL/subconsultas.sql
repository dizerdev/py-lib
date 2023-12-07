USE Clientes;

SELECT * FROM Clientes2016;
SELECT * FROM Clientes2017;


-- Quais clientes na base 2015 tbm estao na base 2016
-- Primeiro SELECT ser� o resultado
SELECT * FROM Clientes2016 AS C16
WHERE
-- O SELECT dentro do bloco EXISTS ser� o filtro
-- para o primeiro SELECT
	EXISTS
	(
		SELECT idCliente FROM Clientes2017 AS C17
		-- Para associar o c�digo entre tabelas
		WHERE C16.idCliente = C17.idCliente
	);


-- Quais clientes na base 2015 que n�o est�o na base 2016
SELECT * FROM Clientes2016 AS C15
WHERE
	NOT EXISTS
	(
		SELECT idCliente FROM Clientes2017 AS C16
		WHERE C15.idCliente = C16.idCliente
	);

USE SisDep;


-- Nome dos funcion�rios que possuam dependentes
SELECT
	F.NomeFuncionario
FROM Funcionario AS F
WHERE 
	F.idMatricula IN (
		SELECT D.idMatricula FROM Dependente AS D
	);


-- Nome dos funcion�rios que n�o possuam dependentes
SELECT
	F.NomeFuncionario
FROM Funcionario AS F
WHERE 
	F.idMatricula NOT IN (
		SELECT D.idMatricula FROM Dependente AS D
	);


-- Retornar funcionarios com salario acima da media
SELECT AVG(Salario) FROM Funcionario;

SELECT 
	NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE Salario > (
	SELECT AVG(Salario) FROM Funcionario
	)