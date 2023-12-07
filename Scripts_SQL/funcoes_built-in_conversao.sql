USE SisDep;

SELECT
	NomeFuncionario,
	CAST(Admissao AS DATE) AS [Admiss�o]
FROM Funcionario;

EXEC sp_help Funcionario;

SELECT 'M�dia Final: ' + CAST(6.5 AS VARCHAR);

--------------------------------------------------------

SELECT
	NomeFuncionario,
	CONVERT(VARCHAR, Admissao, 1) [C�DIGO 1],
	CONVERT(VARCHAR, Admissao, 2) [C�DIGO 2],
	CONVERT(VARCHAR, Admissao, 3) [C�DIGO 3],
	CONVERT(VARCHAR, Admissao, 101) [C�DIGO 101],
	CONVERT(VARCHAR, Admissao, 102) [C�DIGO 102],
	CONVERT(VARCHAR, Admissao, 103) [C�DIGO 103]
FROM Funcionario;

--------------------------------------------------------

SELECT
	NomeFuncionario,
	FORMAT(Salario, 'c', 'pt-br') AS [Em Real],
	FORMAT(Salario, 'C', 'en-us') AS [Em Dolar],
	FORMAT(Admissao, 'd', 'pt-br') AS [Data Brasil],
	FORMAT(Admissao, 'D', 'en-us') AS [Data U.S.],
	FORMAT(Admissao, 'dd - mm - yyyy', 'pt-br') AS [Data Personalizada]
FROM Funcionario;

