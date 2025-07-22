 -- Criação das tabelas
CREATE TABLE autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    data_cadastro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    livro_id INTEGER,
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE,
    data_devolucao_real DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);

-- Inserção de dados
INSERT INTO autores (nome) VALUES
('Machado de Assis'),
('Clarice Lispector'),
('J.K. Rowling');

INSERT INTO livros (titulo, ano_publicacao, autor_id) VALUES
('Dom Casmurro', 1899, 1),
('A Hora da Estrela', 1977, 2),
('Harry Potter e a Pedra Filosofal', 1997, 3);

INSERT INTO usuarios (nome, email) VALUES
('Ana Souza', 'ana@email.com'),
('Carlos Lima', 'carlos@email.com');

INSERT INTO emprestimos (usuario_id, livro_id, data_emprestimo, data_devolucao_prevista) VALUES
(1, 1, '2025-07-01', '2025-07-15'),
(2, 3, '2025-07-10', '2025-07-24');
