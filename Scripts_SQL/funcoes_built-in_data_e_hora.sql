SELECT GETDATE();

USE SisDep;

SELECT
	NomeFuncionario, Admissao,
	DAY(Admissao) AS [Dia da Admissão],
	MONTH(Admissao) AS [Mês da Admissão],
	YEAR(Admissao) AS [Ano da Admissão]
FROM Funcionario;

-- Retornar admitidos na 1a quinzena de qualquer do 2o semestre
-- dos seguintes anos (2000, 2003, 2005, 2008, 2010)

SELECT
	NomeFuncionario, Admissao,
	DAY(Admissao) AS [Dia da Admissão],
	MONTH(Admissao) AS [Mês da Admissão],
	YEAR(Admissao) AS [Ano da Admissão]
FROM Funcionario
WHERE 
	DAY(Admissao) <= 15 AND 
	MONTH(Admissao) >= 7 AND
	YEAR(Admissao) IN (2000, 2003, 2005, 2008, 2010);

----------------------------------------------------------------

SELECT EOMONTH(GETDATE(), 0);
SELECT EOMONTH(GETDATE(), 1);

----------------------------------------------------------------

SELECT DATEFROMPARTS(2017,1,10);

----------------------------------------------------------------
/*
		> YEAR		YYYY
		> QUARTER	Q
		> MONTH		M
		> WEEK		WW
		> DAY		D
*/
SELECT DATEDIFF(DAY, '1993/5/3', GETDATE()) AS [DIAS];
SELECT DATEDIFF(MONTH, '1993/5/3', GETDATE()) AS [MESES];
SELECT DATEDIFF(YEAR, '1993/5/3', GETDATE()) AS [ANOS];
SELECT DATEDIFF(QUARTER, '1993/5/3', GETDATE()) AS [TRIMESTRES];
SELECT DATEDIFF(WEEK, '1993/5/3', GETDATE()) AS [SEMANAS];
SELECT DATEDIFF(HOUR, '1993/5/3', GETDATE()) AS [HORAS];
SELECT DATEDIFF(MINUTE, '1993/5/3', GETDATE()) AS [MINUTOS];
SELECT DATEDIFF(SECOND, '1993/5/3', GETDATE()) AS [SEGUNDOS];

----------------------------------------------------------------

SELECT DATEADD(DAY, 65, GETDATE()) AS [DIAS];
SELECT DATEADD(MONTH, 18, GETDATE()) AS [MESES];
SELECT DATEADD(YEAR, 5, GETDATE()) AS [ANOS];
SELECT DATEADD(WEEK, 20, GETDATE()) AS [TRIMESTRES];
SELECT DATEADD(QUARTER, 3, GETDATE()) AS [SEMANAS];

----------------------------------------------------------------

-- Pedindo conversao de Idioma para o SQL (comando de sessão)
SET LANGUAGE 'ENGLISH';

SELECT
	NomeFuncionario,
	Admissao,
	DATENAME(WEEKDAY, Admissao) AS [Dia da Semana],
	DATENAME(MONTH, Admissao) AS [Mês]
FROM Funcionario;

SET LANGUAGE 'BRAZILIAN';
