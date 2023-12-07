USE SisDep;

SELECT
	NomeFuncionario, Admissao, Salario, Uf, Cidade
FROM Funcionario INNER JOIN Localidade
ON Funcionario.idLocalidade = Localidade.idLocalidade;

SELECT
	NomeFuncionario, Admissao, Salario, Uf, Cidade
FROM Funcionario INNER JOIN Localidade
ON Funcionario.idLocalidade = Localidade.idLocalidade
INNER JOIN Depto
ON Depto.idDepartamento = Funcionario.idDepartamento;

-- Nomes qualificados

SELECT 
	F.NomeFuncionario,
	D.NomeDependente,
	D.NascimentoDependente
FROM Funcionario AS F INNER JOIN Dependente AS D
ON D.idMatricula = F.idMatricula
ORDER BY F.NomeFuncionario;


-- Rotulos ou Alias

SELECT 
	F.NomeFuncionario, D.NomeDependente, D.NascimentoDependente
FROM Funcionario AS F INNER JOIN Dependente AS D
ON D.idMatricula = F.idMatricula
ORDER BY F.NomeFuncionario;