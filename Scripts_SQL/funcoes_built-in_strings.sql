USE SisDep;

SELECT
	NomeFuncionario,
	LEN(NomeFuncionario) AS [N° de Caracteres],
	idMatricula,
	LEFT(idMatricula, 2) AS [Esquerda],
	RIGHT(idMatricula, 2) AS [Direita],
	REPLACE(idMatricula, '10', '20') AS [Substituir],
	CHARINDEX('Silva', NomeFuncionario, 1) AS [Localizar],
	SUBSTRING(NomeFuncionario, 1,CHARINDEX(' ', NomeFuncionario, 1)-1) AS [Primeiro Nome]
FROM Funcionario;
-------------------------------------------------------------------

SELECT RTRIM('Impacta	');
-------------------------------------------------------------------

SELECT LTRIM('	 Impacta');
-------------------------------------------------------------------

SELECT RTRIM(LTRIM('	Impacta		'));
-------------------------------------------------------------------

SELECT 
	UPPER(NomeFuncionario) AS [Maiúsculas],
	LOWER(NomeFuncionario) AS [Minúsculas]
FROM Funcionario;
-------------------------------------------------------------------

SELECT REPLICATE('*', 10);
-------------------------------------------------------------------

SELECT REVERSE(SUBSTRING(REVERSE('Impacta_arquivo.html'), 5, 255));
-------------------------------------------------------------------

SELECT 
	idMatricula, 
	NomeFuncionario, 
	CONCAT(idMatricula, idDepartamento, idCargo) AS [Concatenação],
	idDepartamento, idMatricula
FROM Funcionario;
-------------------------------------------------------------------
SELECT 
	idMatricula, 
	NomeFuncionario, 
	CONCAT(idMatricula, idDepartamento, idCargo) AS [Concatenação],
	idDepartamento, 
	idCargo,
	idMatricula + idDepartamento + idCargo AS [Somados]
	-- é necessario ser texto com texto para concatenar
FROM Funcionario;
