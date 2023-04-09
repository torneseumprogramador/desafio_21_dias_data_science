create database desafio_data_science;

use desafio_data_science;

CREATE TABLE pessoas (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    idade INT NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
