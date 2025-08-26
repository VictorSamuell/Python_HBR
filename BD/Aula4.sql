create schema if not exists Aula4;
use Aula4;

-- Apaga as tabelas se elas já existirem, para começar do zero.
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS autores;

-- Criação da tabela 'autores'
CREATE TABLE autores (
    id int PRIMARY KEY,  -- Em MySQL, use: INT PRIMARY KEY AUTO_INCREMENT
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Criação da tabela 'posts'
CREATE TABLE posts (
    id int PRIMARY KEY AUTO_INCREMENT, -- Em MySQL, use: INT PRIMARY KEY AUTO_INCREMENT
    titulo VARCHAR(200) NOT NULL,
    conteudo TEXT,
    publicado BOOLEAN DEFAULT FALSE,
    data_publicacao DATE,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

-- Inserindo dados na tabela 'autores'
INSERT INTO autores (id, nome, email) VALUES
(1, 'Ana Silva', 'ana.silva@email.com'),
(2, 'Bruno Costa', 'bruno.c@email.com'),
(3, 'Carlos Dias', 'carlos.dias@exemplo.com'),
(4, 'Diana Moreira', 'diana.m@email.com'),
(5, 'Eduardo Faria', 'edu.faria@exemplo.com'),
(6, 'Fernanda Lima', 'f.lima@outroemail.com'),
(7, 'Gabriel Souza', 'g.souza@email.com');


-- Inserindo dados na tabela 'posts'
-- (Note que as datas estão no formato 'AAAA-MM-DD')
INSERT INTO posts (titulo, conteudo, publicado, data_publicacao, autor_id) VALUES
('Introdução ao SQL', 'Neste post, vamos aprender o básico do SQL...', TRUE, '2024-01-10', 1),
('Modelagem de Dados', 'Um guia completo sobre modelagem de bancos de dados relacionais.', TRUE, '2024-01-15', 2),
('Avançando com Python', 'Dicas e truques para programadores Python intermediários.', TRUE, '2024-02-01', 1),
('O que há de novo em tecnologia?', 'Análise das principais tendências de tecnologia para este ano.', TRUE, '2024-02-20', 4),
('Rascunho do post sobre nuvem', 'Explorando os serviços de AWS, Azure e GCP...', FALSE, '2024-03-05', 3),
('SQL para Análise de Dados', 'Como usar SQL para extrair insights valiosos.', TRUE, '2024-03-12', 2),
('Gerenciamento de Projetos Ágeis', 'Scrum e Kanban na prática.', TRUE, '2024-04-01', 5),
('A importância da segurança digital', 'Proteja seus dados contra ameaças.', TRUE, '2024-04-25', 4),
('Revisão do novo framework JS', 'Este post ainda precisa ser revisado.', FALSE, '2024-05-10', 1),
('Carreira em tecnologia: por onde começar?', 'Um guia para iniciantes na área de TI.', TRUE, '2024-05-18', 7),
('Receitas com poucos ingredientes', 'Cozinhando de forma fácil e rápida.', TRUE, '2024-06-02', 6),
('Como otimizar queries SQL', 'Melhorando a performance do seu banco de dados.', TRUE, '2024-06-15', 2),
('Guia de Viagem para a Patagônia', 'Dicas de roteiro, hospedagem e passeios.', TRUE, '2024-07-01', 5),
('Entendendo Machine Learning', 'Conceitos fundamentais para quem quer iniciar na área.', TRUE, '2024-07-22', 4),
('Post de teste (não publicar)', 'Apenas um teste de sistema.', FALSE, '2024-08-01', 3),
('Desenvolvimento Web Moderno', 'Construindo aplicações com React e Node.js.', TRUE, '2023-11-20', 1),
('Finanças Pessoais para Iniciantes', 'Como organizar seu orçamento e começar a investir.', TRUE, '2023-12-05', 7),
('A História da Computação', 'Dos primeiros computadores à era da internet.', TRUE, '2023-10-15', 2),
('Dicas de Produtividade', 'Como ser mais produtivo no trabalho remoto.', TRUE, '2023-09-01', 5),
('Introdução à jardinagem', 'Como cuidar das suas primeiras plantas.', TRUE, '2023-08-10', 6),
('Análise de Mercado Financeiro', 'Tendências para o segundo semestre.', TRUE, '2024-08-15', 4);

/*
Exercícios e Respostas
Exercício 1: Selecione apenas as colunas nome e email de todos os registros da tabela autores. 
Exercício 2: Encontre todos os posts que não foram publicados. 

Exercício 3: Liste o título de todos os posts cujo autor_id seja igual a 1. 

Exercício 4: Encontre todos os autores cujo nome começa com a letra 'A'. 

Exercício 5: Selecione todos os posts publicados que foram escritos pelo autor com autor_id = 2. 
Exercício 6: Liste todos os posts, ordenando-os pela data de publicação, do mais antigo para o mais recente. 
Exercício 7: Encontre os 5 posts mais recentes que foram publicados. 

Exercício 8: Selecione todos os autores cujos IDs sejam 2, 4 ou 7. 

Exercício 9: Encontre todos os posts cujo título contenha a palavra 'tecnologia' (em qualquer parte do título). 
Exercício 10: Mostre o segundo conjunto de 10 posts quando ordenados por título em ordem alfabética (útil para a página 2 de uma lista). 

*/
-- EXERCICIO 1
select nome,email from autores;

-- EXERCICIO 2
select * from posts where publicado=FALSE;

-- EXERCICIO 3
select titulo from posts where autor_id = 1;

-- EXERCICIO 4
select * from autores where nome like "A%";

-- EXERCICIO 5
select * from posts where publicado = TRUE and autor_id = 2;

-- EXERCICIO 6
select * from posts order by data_publicacao ASC;

-- EXERCICIO 7
select * from posts order by data_publicacao ASC limit 5;

-- EXERCICIO 8
select * from autores where id in(2,4,7);

-- EXERCICIO 9
select * from posts where titulo like "%TECNOLOGIA%";

-- EXERCICIO 10
select * from posts order by titulo ASC limit 10 offset 10;
select * from posts order by titulo ASC limit 10,20;
