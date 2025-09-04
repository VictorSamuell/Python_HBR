# import mysql.connector as mysql
#
# bd = mysql.connect(host='localhost', user ='root',
# passwd = 'ifsp')
#
# cursor = bd.cursor()

# cursor.execute('CREATE DATABASE ifsp2')

# cursor.execute('SHOW DATABASES')
# bases = cursor.fetchall()
# print(bases)

# cursor.execute('use ifsp2')
# cursor.execute('CREATE TABLE '
# 'aula9(id int not null auto_increment '
# 'primary key,nome varchar(100),'
# 'nota numeric(2,1))')

# comando = 'INSERT INTO aula9(nome, nota) VALUES (%s, %s)'
# valores = [("Pedro",4.5),("Adrian",7.8),("Camila",9.9)]
# cursor.executemany(comando,valores)
# bd.commit()


# consulta = 'SELECT * FROM aula9'
# cursor.execute(consulta)
# registros = cursor.fetchall()
# for reg in registros:
#     print(reg)


# deletar = 'DELETE FROM aula9 WHERE id=11'
# cursor.execute(deletar)
# bd.commit()


#
# atualizar = "UPDATE aula9 SET nome='Carlos' WHERE id=10"
# cursor.execute(atualizar)
# bd.commit()
#
# cursor.close()
# bd.close()


import mysql.connector as mysql
from mysql.connector import Error

try:
    bd = mysql.connect(host='localhost', database='iftm2', user='root', password='Info@123')

    if bd.is_connected():
        versao = bd.get_server_info()
        print('Conectado ao MySQL Server versão ', versao)
        cursor = bd.cursor()
        cursor.execute('SELECT DATABASE();')
        resultado = cursor.fetchone()
        print('Você está conectado ao banco de dados: ', resultado)
except Error as e:
    print('Erro ao conectar o MySQL', e)
finally:
    if (bd.is_connected()):
        cursor.close()
        bd.close()
        print('Conexão MySQL está fechado')
