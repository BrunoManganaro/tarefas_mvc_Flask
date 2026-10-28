DROP DATABASE IF EXISTS 'tarefas';

CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

DROP TABLE IF EXISTS `tarefas`;

CREATE TABLE IF NOT EXISTS `tarefas` (
    `id_caneta` BIGINT NOT NULL PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusao` DATETIME NULL      
);