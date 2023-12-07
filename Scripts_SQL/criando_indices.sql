USE curso_impacta;

-- visualizar indices

EXEC sp_help tblEstoque;

-- Criando indice

CREATE NONCLUSTERED INDEX IX_tblEstoque 
ON tblEstoque(dataEntrada DESC);

EXEC sp_helpindex tblEstoque;

DROP INDEX IX_tblEstoque
ON tblEstoque;