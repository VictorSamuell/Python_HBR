-- drop schema aula1;
-- create schema if not exists aula1;
-- use aula1;


-- create table Autor(
-- 	id_autor int not null primary key,
--     nome varchar(60) not null,
--     email varchar(30) not null
    
-- );

-- create table Post(
-- 	id_post int not null primary key,
--     titulo varchar(50) not null,
--     conteudo varchar(200) not null,
--     data_publicacao date not null,
--     id_autor int not null ,
--     CONSTRAINT fk_autor FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
-- );

-- create table Comentario(
-- 	id_comentario int not null primary key,
--     texto varchar(300) not null,
--     data_comentario date not null,
--     autor_comentario varchar(50) not null,
--     id_post int not null,
--     CONSTRAINT fk_post FOREIGN KEY (id_post) REFERENCES Post(id_post)
-- );

-- alter table autor add column cpf varchar(20) not null;

-- # drop table Post;
-- # drop table Comentario;
-- # drop table Autor;

-- select * from autor;


-- drop schema aula1;
-- create schema if not exists aula1;
-- use aula1;


-- create table __Log__(
-- 	codigoLog int not null primary key,
--     nome varchar(50) not null
-- );

-- create table Sessão(
-- 	codigoSes int not null primary key,
--     usuario varchar(30) NOT NULL,
--     ip varchar(15) not null,
-- 	codigoLog int not null,
--     CONSTRAINT fk_log foreign key (codigoLog) REFERENCES __Log__(codigoLog)
-- );

-- create table Pagina(
-- 	codigoPag int not null primary key,
--     codigo_html varchar(1000) not null,
--     tipo_de_conteudo varchar(60) not null,
--     titulo varchar(50) not null,
--     tamanho_real varchar(60) not null,
--     url varchar(1000) not null,
--     tamanho_do_arquivo float not null,
--     texto_puro varchar(200) not null
    
-- );

-- create table Requisição(
-- 	codigoReq int not null primary key,
--     codigo_http varchar(10) not null,
--     tempo_transcorrido int not null,
--     carimbo_de_tempo int not null,
--     codigoSes int not null,
--     codigoPag int not null,
--     CONSTRAINT fk_sessao foreign key (codigoSes) REFERENCES Sessão(codigoSes),
--     CONSTRAINT fk_pagina foreign key (codigoPag) REFERENCES Pagina(codigoPag)
-- );

-- create table Link(
-- 	codigoLink int not null primary key,
--     url varchar(1000) not null,
--     vizinhança varchar(300) not null,
--     texto varchar(300) not null,
--     codigoPag int not null,
--     CONSTRAINT fk_pagina2 foreign key (codigoPag) REFERENCES Pagina(codigoPag)
-- );



-- --