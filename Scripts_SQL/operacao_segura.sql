USE SeguroVeiculo;

SELECT * FROM Apolices;

-- Iniciar uma transação
BEGIN TRAN
-- Verificar se há alguma transação ativa
-- TRANCOUNT retorna num int
SELECT @@TRANCOUNT;

-- Todos valores serão alterados
UPDATE Apolices 
SET valorApolice = valorApolice + 1500;

-- Desfazer
ROLLBACK TRANSACTION

-- Operação segura
BEGIN TRAN
	UPDATE Apolices
	SET valorApolice = valorApolice + 1500
	WHERE nContrato = 1000;

-- Confirmar operação
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