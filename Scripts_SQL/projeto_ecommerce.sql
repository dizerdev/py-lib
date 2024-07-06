CREATE TABLE IF NOT EXISTS TB_CADASTRO
(
    COD_CADASTRO SERIAL PRIMARY KEY NOT NULL,
    NOME_COMPLETO_CAD VARCHAR(50) NOT NULL,
    E_MAIL VARCHAR(50) UNIQUE NOT NULL,
    SENHA VARCHAR(64) NOT NULL,
    DATA_CADASTRO TIMESTEMP DEFAULT NOW()
)

CREATE TABLE IF NOT EXISTS TB_CLIENTE
(
    COD_CLIENTE SERIAL PRIMARY KEY NOT NULL,
    NOME_COMPLETO_CLI VARCHAR(50) NOT NULL,
    E_MAIL VARCHAR(50) UNIQUE NOT NULL,
    ENDERECO_CLI VARCHAR(60) NOT NULL,
    REFERENCIA VARCHAR(60),
    BAIRRO_CLI VARCHAR(20) NOT NULL,
    CIDADE_CLI VARCHAR(20) NOT NULL,
    ESTADO_CLI VARCHAR(2) NOT NULL,
    CEP_CLI VARCHAR(8) NOT NULL,
    TELEFONE_CLI VARCHAR(11) NOT NULL,
    DATA_CADASTRO TIMESTEMP DEFAULT NOW()
)

CREATE TABLE IF NOT EXISTS TB_PRODUTO
(
    COD_PRODUTO SERIAL PRIMARY KEY NOT NULL,
    DESCRICAO VARCHAR(60),
    COD_CATEGORIA INTEGER,
    QTD_ESTOQUE NUMERIC(12,2),
    PRECO_CUSTO NUMERIC(12,2),
    PRECO_VENDA NUMERIC(12,2),
    CARACTERISTICAS VARCHAR(200),
)

CREATE TABLE IF NOT EXISTS TB_CATEGORIA
(
    COD_CATEGORIA SERIAL PRIMARY KEY NOT NULL,
    CATEGORIA VARCHAR(30) NOT NULL,
)

CREATE TABLE IF NOT EXISTS TB_PEDIDO
(
    NUM_PEDIDO SERIAL PRIMARY KEY NOT NULL,
    COD_CLIENTE 
    NUM_ITEM INTEGER NOT NULL,
    
)