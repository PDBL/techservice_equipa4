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
    SELECT
        id_prioridade,
        nome,
        descricao,
        nivel,
        ativo
    FROM prioridade_os
    WHERE ativo = 1
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
        FROM prioridade_os
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
    SET
        nome=%s,
        descricao=%s,
        nivel=%s,
        ativo=%s
    WHERE id_prioridade=%s
    """
    valores = (
    prioridade.nome,
    prioridade.descricao,
    prioridade.nivel,
    prioridade.ativo,
    prioridade.id_prioridade
)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def excluir(id_prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE prioridade_os
    SET ativo = 0
    WHERE id_prioridade=%s
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
            ativo = 1
        WHERE id_prioridade = %s
    """

    cursor.execute(sql, (id_prioridade,))
    conexao.commit()

    cursor.close()
    conexao.close()

def contar():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM prioridade_os
        WHERE ativo=1
        """
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return total