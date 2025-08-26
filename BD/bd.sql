drop schema aula1;
create schema if not exists aula1;
use aula1;


create table Autor(
	id_autor int not null primary key,
    nome varchar(60) not null,
    email varchar(30) not null
    
);

create table Post(
	id_post int not null primary key,
    titulo varchar(50) not null,
    conteudo varchar(200) not null,
    data_publicacao date not null,
    id_autor int not null ,
    CONSTRAINT fk_autor FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
);

create table Comentario(
	id_comentario int not null primary key,
    texto varchar(300) not null,
    data_comentario date not null,
    autor_comentario varchar(50) not null,
    id_post int not null,
    CONSTRAINT fk_post FOREIGN KEY (id_post) REFERENCES Post(id_post)
);

alter table autor add column cpf varchar(20) not null;

# drop table Post;
# drop table Comentario;
# drop table Autor;

select * from autor;


