import sqlite3

def cadastrar_militar(nome, idade, posto_grad, especialidade):
    # Conectar-se ao banco de dados
    conexao = sqlite3.connect('banco_dados.db')
    cursor = conexao.cursor()

    # Executar a inserção dos dados na tabela de militares
    cursor.execute('INSERT INTO militares (nome, idade, posto_grad, especialidade) VALUES (?, ?, ?, ?)',
                   (nome, idade, posto_grad, especialidade))

    # Salvar as alterações e fechar a conexão com o banco de dados
    conexao.commit()
    conexao.close()