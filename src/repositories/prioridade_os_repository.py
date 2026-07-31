from src.database.conexao import conectar

def inserir(prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO prioridade_os (nome, descricao, nivel, ativo)
        VALUES (%s, %s, %s, %s)
    """
    valores = (prioridade.nome, prioridade.descricao, prioridade.nivel, prioridade.ativo)

    cursor.execute(sql, valores)
    conexao.commit()
    prioridade.id_prioridade = cursor.lastrowid

    cursor.close()
    conexao.close()
    return prioridade

def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_prioridade, nome, descricao, nivel, ativo)
        FROM prioridades_os
        ORDER BY nome
    """

    cursor.execute(sql)
    prioridade = cursor.fetchall()

    cursor.close()
    conexao.close()
    return prioridade

def procurar_por_id(id_prioridade):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM prioridade_os
        WHERE id_prioridade = %s
    """

    cursor.execute(sql, (id_prioridade,))
    prioridade = cursor.fetchone()

    cursor.close()
    conexao.close()
    return prioridade


def procurar_por_nome(nome):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM prioridade
        WHERE nome LIKE %s
        ORDER BY nome
    """

    cursor.execute(sql, ("%" + nome + "%",))
    prioridade = cursor.fetchall()

    cursor.close()
    conexao.close()
    return prioridade

def atualizar(prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE prioridade_os
        SET nome = %s,
            descricao = %s,
            nivel = %s,
        WHERE id_cliente = %s
          AND status = 1
    """
    valores = (prioridade.nome, prioridade.descricao, prioridade.nivel. prioridade.ativo)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def excluir(id_prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE prioridade
        SET nivel = 3,
        WHERE id_prioridade = %s
          AND status = 1
    """

    cursor.execute(sql, (id_prioridade,))
    conexao.commit()

    cursor.close()
    conexao.close()

def restaurar(id_prioridade):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE prioridade_os
        SET
            nivel = 1,
        WHERE id_prioridade = %s
    """

    cursor.execute(sql, (id_prioridade,))
    conexao.commit()

    cursor.close()
    conexao.close()

