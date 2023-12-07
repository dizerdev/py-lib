USE SisDep;

-- Retornar o total geral de salarios pagos
SELECT SUM(Salario) AS [Total de Sal�rios] FROM Funcionario;

-- Retornar a m�dia de salarios
SELECT AVG(Salario) AS [M�dia Salarial] FROM Funcionario;

-- Mais de uma agregacao no mesmo comando SELECT
SELECT 
	MAX(Salario) AS [Maior Sal�rio],
	MIN(Salario) AS [Menor Sal�rio],
	COUNT(Salario) AS [N� de Funcion�rios]
FROM Funcionario;

USE SysConVendas;
SELECT * FROM Dados;

SELECT COUNT(Vendedor) AS Contagem_coluna FROM Dados;
SELECT COUNT(Pedido) AS Contagem_coluna FROM Dados;
SELECT COUNT(*) AS Contagem_Linha FROM Dados;