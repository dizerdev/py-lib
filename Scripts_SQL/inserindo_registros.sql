USE Consessionaria;

EXEC sp_help tblModelos;
-- Insert Posicional

INSERT INTO tblMarcas
VALUES('FIAT');

-- Inserção de várias linhas
INSERT INTO tblMarcas
VALUES('FORD'),('CHEVROLET'),('VOLKSWAGEN'),('HONDA');

-- Visualizar o dado
SELECT * FROM tblMarcas;

-- Inserção declarativa
INSERT INTO tblModelos
(idMarca, nomeModelo)
VALUES 
(4, 'Onix'),(1, 'Uno'),(3, 'Eco Sport');

SELECT * FROM tblMarcas;

INSERT INTO tblEstoque
([idModelo], [dataEntrada], [precoEstoque])
VALUES
(1, '2023-05-03', 15000);

SELECT * FROM tblEstoque;