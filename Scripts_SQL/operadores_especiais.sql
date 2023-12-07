-- Operadores especiais
USE SisDep;
-- BETWEEN
SELECT
	idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE Salario BETWEEN 2000 AND 4000;

SELECT
	idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE idDepartamento BETWEEN '7' AND '10';

SELECT
	idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE idDepartamento NOT BETWEEN '7' AND '10';

-- IN
SELECT 
	idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE idDepartamento IN(1, 3, 5, 6, 10);

SELECT 
	idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE idDepartamento NOT IN(1, 3, 5, 6, 10)
ORDER BY 1;

SELECT * FROM Funcionario;

-- LIKE
/* 
	Caracteres coringa

	% = 1 ou mais caracteres desconhecidos
	_ = somente 1 caractere desconhecido
*/

SELECT 
	idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE NomeFuncionario LIKE 'A%'
ORDER BY NomeFuncionario;

SELECT 
	idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario		
WHERE NomeFuncionario LIKE 'A_A%'
ORDER BY NomeFuncionario;

SELECT 
	idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE NomeFuncionario LIKE '%OLIVEIRA'
ORDER BY NomeFuncionario;

SELECT 
	idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
WHERE NomeFuncionario LIKE '%SILVA%'
ORDER BY NomeFuncionario;