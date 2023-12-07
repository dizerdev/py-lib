-- Tabela temporaria #LOCAL (CREATE TABLE)
-- Dentro de tempdb
CREATE TABLE #Clientes
(
	codigo		int,
	nomeCliente	varchar(50),
	cadastro	date
)

SELECT * FROM #Clientes

INSERT INTO #Clientes
VALUES
	(1,'Diego', '2023/05/09'),
	(2,'Lucia', '2023/05/09');

-----------------------------------------------

USE SysConVendas;
-- Lendo DISCO RÍGIDO
SELECT * FROM Dados;
-- Criando tabela na RAM
SELECT * 
INTO #Pesquisa1
FROM Dados;
-- Lendo RAM
SELECT * FROM #Pesquisa1;
-- MAIS PERFORMANCE

-- Filtros
SELECT * FROM #Pesquisa1
WHERE Mes = 'agosto';

-- Atualizando
UPDATE #Pesquisa1
SET Vendedor = 'Hélio'
WHERE Pedido = 21794;

-- Para tornar essa tabela segura GLOBAL
SELECT *
INTO ##Pesquisa2
FROM Dados
WHERE Regiao = 'Sudeste';

SELECT * FROM ##Pesquisa2;