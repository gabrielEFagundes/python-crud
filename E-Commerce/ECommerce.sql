CREATE DATABASE ecommerce;
USE ecommerce;

CREATE TABLE produtos(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10,2) NOT NULL,
    estoque INT NOT NULL,
    avaliacao NUMERIC(1,1) NOT NULL,
    categoria VARCHAR(100)
);

# Testes
TRUNCATE produtos;

DROP DATABASE ecommerce;