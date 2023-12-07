USE SysConVendas

SELECT * FROM Dados;

BEGIN TRAN
	UPDATE Dados
	SET Vendedor = NULL
	WHERE Pedido IN(21768,21781,21794,21807);
COMMIT


-- FUNCAO ISNULL
SELECT
	Pedido, 
	ISNULL(Vendedor,'Sem informação') AS Vendedor, 
	Produto, 
	Total
FROM Dados;
-- OU
SELECT
	Pedido, 
	ISNULL(Vendedor,'') AS Vendedor, 
	Produto, 
	Total
FROM Dados;


-- FILTRAR NULOS E NAO NULOS
SELECT
	Pedido, 
	Vendedor, 
	Produto, 
	Total
FROM Dados
WHERE Vendedor IS NULL;
-- OU
SELECT
	Pedido, 
	Vendedor, 
	Produto, 
	Total
FROM Dados
WHERE Vendedor IS NOT NULL;


-- FUNCAO COALESCE
CREATE TABLE Cotacao
(
	codigo		int		identity,
	produto		varchar(50)		not null,
	cotacao1	money			null,
	cotacao2	money			null,
	cotacao3	money			null,
)

INSERT INTO Cotacao
VALUES
('Mouse', NULL, 25, NULL),
('Impressora', 200, NULL, 350),
('Monitor', NULL, NULL, 500),
('HD Externo', NULL, NULL, NULL);

SELECT * FROM Cotacao;

-- TRAS O PRIMEIRO VALOR NAO NULO
SELECT 
	produto,
	COALESCE(cotacao1, cotacao2, cotacao3, 0) AS Cotacao
FROM Cotacao;
-- OU PARA ACHAR QUAL É IGUAL A 0
SELECT * FROM Cotacao
WHERE COALESCE(cotacao1, cotacao2, cotacao3, 0) = 0;
