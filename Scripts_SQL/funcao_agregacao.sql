USE SisDep;

-- Retornar o total geral de salarios pagos
SELECT SUM(Salario) AS [Total de Salários] FROM Funcionario;

-- Retornar a média de salarios
SELECT AVG(Salario) AS [Média Salarial] FROM Funcionario;

-- Mais de uma agregacao no mesmo comando SELECT
SELECT 
	MAX(Salario) AS [Maior Salário],
	MIN(Salario) AS [Menor Salário],
	COUNT(Salario) AS [N° de Funcionários]
FROM Funcionario;

USE SysConVendas;
SELECT * FROM Dados;

SELECT COUNT(Vendedor) AS Contagem_coluna FROM Dados;
SELECT COUNT(Pedido) AS Contagem_coluna FROM Dados;
SELECT COUNT(*) AS Contagem_Linha FROM Dados;