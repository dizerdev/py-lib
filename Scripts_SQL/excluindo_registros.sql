USE Consorcio;

SELECT * FROM Carteiras;

DELETE FROM Carteiras
WHERE Cpf = 31439373721;

DELETE FROM Carteiras
WHERE Uf = 'GO';

USE SisDep;

-- Exclus�o bem sucedida
DELETE FROM Funcionario
WHERE idMatricula = 1001;

-- Exclus�o mal sucedida
DELETE FROM Funcionario
WHERE idMatricula = 1000;