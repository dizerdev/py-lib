USE SisDep;

SELECT 
	F.NomeFuncionario,
    D.NomeDependente, 
	D.NascimentoDependente
FROM Funcionario AS F INNER JOIN Dependente AS D
ON F.idMatricula = D.idMatricula
ORDER BY F.NomeFuncionario ASC;


SELECT
	F.NomeFuncionario,
	C.NomeCargo,
	F.Salario	
FROM Funcionario AS F RIGHT JOIN Cargo AS C
ON F.idCargo = C.idCargo
WHERE F.NomeFuncionario IS NULL;