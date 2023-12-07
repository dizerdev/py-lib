USE SisDep;

-- Todas as colunas de uma tabela
SELECT * FROM Funcionario;

-- Somente algumas colunas
SELECT idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
ORDER BY NomeFuncionario ASC;

SELECT idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
ORDER BY Salario DESC;

-- Ordenar mais de uma coluna

SELECT idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
ORDER BY idDepartamento ASC, Salario DESC;

-- TOP rank

SELECT TOP 10 PERCENT idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
ORDER BY Salario DESC;

-- Com empates
SELECT TOP 9 WITH TIES idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
FROM Funcionario
ORDER BY Salario DESC;