USE SeguroVeiculo;

SELECT * FROM Apolices;

-- Iniciar uma transa��o
BEGIN TRAN
-- Verificar se h� alguma transa��o ativa
-- TRANCOUNT retorna num int
SELECT @@TRANCOUNT;

-- Todos valores ser�o alterados
UPDATE Apolices 
SET valorApolice = valorApolice + 1500;

-- Desfazer
ROLLBACK TRANSACTION

-- Opera��o segura
BEGIN TRAN
	UPDATE Apolices
	SET valorApolice = valorApolice + 1500
	WHERE nContrato = 1000;

-- Confirmar opera��o
-- Depois de 
COMMIT TRAN;

USE SisDep;

BEGIN TRAN 
	UPDATE Funcionario
	SET Salario = Salario * 1.1
	OUTPUT
		deleted.idMatricula,
		deleted.NomeFuncionario,
		deleted.Salario AS [SalarioAnterior],
		inserted.Salario AS [NovoSalario]
	WHERE Salario <= 3000;

COMMIT;