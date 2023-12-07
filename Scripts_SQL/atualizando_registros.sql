USE SisDep;

-- Bonus de R$ 100 para todos os funcionarios
UPDATE Funcionario
SET salario = salario + 100;

SELECT * FROM Funcionario;

EXEC SP_HELP Funcionario;


-- Reajuste de 10% para todos os funcionários
UPDATE Funcionario
SET Salario = Salario * 0.1 + Salario;

-- Operador Composto
-- SET Salario *= 1.1;

-- Atualizar mais de uma coluna simultaneamente
-- Com condição WHERE

UPDATE Funcionario
SET Salario = Salario * 1.05, 
	idCargo = 2 WHERE idMatricula = 1000;

-- MUITO CUIDADO, NÃO EXISTE CTRL + Z NO SQL
