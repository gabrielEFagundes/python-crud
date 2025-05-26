CREATE DATABASE ConsultaMedica;
USE consultaMedica;

CREATE TABLE paciente(
	id_paciente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE medico(
	id_medico INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100) NOT NULL
);

CREATE TABLE consultas(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    status ENUM("confirmada", "cancelada") NOT NULL,
    id_paciente_fk INT,
    id_medico_fk INT,
    FOREIGN KEY(id_paciente_fk) REFERENCES Paciente(id_paciente),
    FOREIGN KEY(id_medico_fk) REFERENCES Medico(id_medico)
);

# uso para testes
TRUNCATE paciente;
TRUNCATE medico;
TRUNCATE consultas;

DROP DATABASE ConsultaMedica;