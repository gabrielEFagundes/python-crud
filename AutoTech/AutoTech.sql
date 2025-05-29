CREATE DATABASE autotech;
USE autotech;

CREATE TABLE pecas(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    peso NUMERIC(10,2) NOT NULL,
    lote INT NOT NULL,
    data_fabricacao DATE NOT NULL,
    setor VARCHAR(100)
);

# Testes
TRUNCATE pecas;

DROP DATABASE autotech;