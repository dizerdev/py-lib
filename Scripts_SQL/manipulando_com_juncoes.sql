USE SisDep;

-- Bonus de 100 reais para todos os funcionarios que possuam dependentes

BEGIN TRAN
	UPDATE Funcionario
	SET Salario = Salario + 100
	FROM Funcionario AS F INNER JOIN Dependente AS D
	ON F.idMatricula = D.idMatricula;

ROLLBACK
COMMIT

-- Bonus de 10% para todos os funcionarios que não possuam dependentes

SELECT 
	F.NomeFuncionario, D.NomeDependente
FROM Funcionario AS F LEFT JOIN Dependente AS D
ON F.idMatricula = D.idMatricula
WHERE D.NomeDependente IS NULL;


BEGIN TRAN
	UPDATE Funcionario
	SET Salario = Salario + 1.1
	FROM Funcionario AS F LEFT JOIN Dependente AS D
	ON F.idMatricula = D.idMatricula
	WHERE D.NomeDependente IS NULL;
ROLLBACK
COMMIT

-- Desligamento de funcionários do dpto SAC com salário acima de 1500 reais

BEGIN TRAN
	DELETE Funcionario
	FROM Funcionario  AS F INNER JOIN Depto AS D
	ON F.idDepartamento = D.idDepartamento
	WHERE D.NomeDepartamento = 'SAC' AND F.Salario > 1500;
ROLLBACK
COMMIT

-- Desligamento de funcionarios com salario superior a 4k sem dependentes

BEGIN TRAN
	DELETE Funcionario
	FROM Funcionario AS F LEFT JOIN Dependente AS D
	ON F.idMatricula = D.idMatricula
	WHERE D.NomeDependente IS NULL AND F.Salario > 4000;

ROLLBACK
COMMIT
