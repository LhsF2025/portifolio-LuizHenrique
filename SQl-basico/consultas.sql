-- Livros emprestados com nomes dos usuários
SELECT u.nome AS usuario, l.titulo, e.data_emprestimo
FROM emprestimos e
JOIN usuarios u ON e.usuario_id = u.id
JOIN livros l ON e.livro_id = l.id;

-- Livros com nomes dos autores
SELECT l.titulo, a.nome AS autor
FROM livros l
JOIN autores a ON l.autor_id = a.id;

-- Empréstimos ainda pendentes
SELECT * FROM emprestimos WHERE data_devolucao_real IS NULL;
