drop schema aula1;
create schema if not exists aula1;
use aula1;


create table __Log__(
	codigoLog int not null primary key,
    nome varchar(50) not null
);

create table Sessão(
	codigoSes int not null primary key,
    usuario varchar(30) NOT NULL,
    ip varchar(15) not null,
	codigoLog int not null,
    CONSTRAINT fk_log foreign key (codigoLog) REFERENCES __Log__(codigoLog)
);

create table Pagina(
	codigoPag int not null primary key,
    codigo_html varchar(1000) not null,
    tipo_de_conteudo varchar(60) not null,
    titulo varchar(50) not null,
    tamanho_real varchar(60) not null,
    url varchar(1000) not null,
    tamanho_do_arquivo float not null,
    texto_puro varchar(200) not null
    
);

create table Requisição(
	codigoReq int not null primary key,
    codigo_http varchar(10) not null,
    tempo_transcorrido int not null,
    carimbo_de_tempo int not null,
    codigoSes int not null,
    codigoPag int not null,
    CONSTRAINT fk_sessao foreign key (codigoSes) REFERENCES Sessão(codigoSes),
    CONSTRAINT fk_pagina foreign key (codigoPag) REFERENCES Pagina(codigoPag)
);

create table Link(
	codigoLink int not null primary key,
    url varchar(1000) not null,
    vizinhança varchar(300) not null,
    texto varchar(300) not null,
    codigoPag int not null,
    CONSTRAINT fk_pagina2 foreign key (codigoPag) REFERENCES Pagina(codigoPag)
);



--