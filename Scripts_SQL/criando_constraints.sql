USE curso_impacta;

CREATE TABLE tblEstoque
(
	idEstoque		int			identity
	Constraint PK_tblEstoque_idEstoque
	Primary Key (idEstoque),

	idModelo		int			not null
	Constraint FK_tblEstoque_tblModelos
	Foreign Key (idModelo)
	References tblModelos(idModelo),

	dataEntrada		date		Default GETDATE(),

	precoEstoque	money		not null
	Constraint CK_tblEstoque_precoEstoque
	CHECK (precoEstoque >= 10000.00 AND precoEstoque <= 200000)
);

EXEC sp_help tblEstoque

ALTER TABLE tblEstoque
ADD placa char(8);

ALTER TABLE tblEstoque
ALTER COLUMN placa char(7);

ALTER TABLE tblEstoque
DROP COLUMN placa;

ALTER TABLE tblEstoque
DROP CONSTRAINT CK_tblEstoque_precoEstoque;

ALTER TABLE tblEstoque
DROP COLUMN precoEstoque;

ALTER TABLE tblEstoque
ADD precoEstoque	money		not null
Constraint CK_tblEstoque_precoEstoque
CHECK (precoEstoque >= 10000.00 AND precoEstoque <= 200000);