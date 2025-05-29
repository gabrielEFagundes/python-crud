CREATE DATABASE ClinicaMedica;
USE ClinicaMedica;

CREATE TABLE pacientes(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    ultima_consulta DATE,
    tipo_sanguineo VARCHAR(3) NOT NULL,
    historico VARCHAR(255) NOT NULL
);

# Testes
TRUNCATE pacientes;

DROP DATABASE ClinicaMedica;

SELECT * FROM pacientes WHERE ultima_consulta >= CURDATE() - INTERVAL 30 DAY