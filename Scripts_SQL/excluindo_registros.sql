USE Consorcio;

SELECT * FROM Carteiras;

DELETE FROM Carteiras
WHERE Cpf = 31439373721;

DELETE FROM Carteiras
WHERE Uf = 'GO';

USE SisDep;

-- Exclusão bem sucedida
DELETE FROM Funcionario
WHERE idMatricula = 1001;

-- Exclusão mal sucedida
DELETE FROM Funcionario
WHERE idMatricula = 1000;