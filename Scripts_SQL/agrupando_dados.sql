USE SysConVendas;
SELECT * FROM DADOS;

SELECT 
	Cidade,SUM(Total) AS [Faturamento Total] 
FROM Dados
GROUP BY Cidade;

-- Com 2 ou mais grupos
SELECT 
	Produto,Cidade,SUM(Total) AS [Faturamento Total],
	COUNT(*) AS [N° de Ocorrências]
FROM Dados
GROUP BY Produto, Cidade;

-- Filtros em Agrupamento HAVING
SELECT 
	Cidade,SUM(Total) AS [Faturamento Total] 
FROM Dados
GROUP BY Cidade
HAVING SUM(Total) > 20000
ORDER BY 2;

-- Subtotais (linha extra)
SELECT 
	Cidade,SUM(Total) AS [Faturamento Total] 
FROM Dados
GROUP BY Cidade
WITH ROLLUP;

-- Com 2 grupos
SELECT 
	Cidade, Produto,SUM(Total) AS [Faturamento Total] 
FROM Dados
GROUP BY Cidade, Produto
WITH ROLLUP;

-- Com cube por todas colunas nao agregadas no SELECT
SELECT 
	Cidade, Produto,SUM(Total) AS [Faturamento Total] 
FROM Dados
GROUP BY Cidade, Produto
WITH CUBE;

-----------------------------------------------------------
USE SisDep;

-- Agrupamento com juncoes

SELECT
	NomeFuncionario, COUNT(*) [N° de Dependentes]
FROM Funcionario AS F INNER JOIN Dependente AS D
ON F.idMatricula = D.idMatricula
GROUP BY NomeFuncionario;