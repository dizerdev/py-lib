USE curso_impacta;

--criando tabelas

CREATE TABLE tblMarcas
--unique cria constrain com hexadecimal
(
	idMarca			int				identity		primary key,
	nomeMarca		nchar(20)		Not Null		unique
);
--identity = autonumerado
--Visualizando estrutura de tabelas
EXEC sp_help tblMarcas;

CREATE TABLE tblModelos
(
	idModelo		int				identity,
	Constraint	PK_tblModelos_idModelo
	Primary Key (idModelo),

	idMarca			int				Not Null
	Constraint FK_tblModelos_tblMarcas
	Foreign Key(idMarca) References tblMarcas(idMarca),

	nomeModelo		nchar(30)		Not Null
	Constraint UQ_tblModelos_nomeModelo
	Unique (nomeModelo)
);

EXEC sp_help tblModelos;