import pymysql

host = "localhost"
user = "root"
password = ""
database = ""


def connect():
    return pymysql.connect(host, user, password, database)


def executor(sql, values):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
    finally:
        connection.commit()
        connection.close()


def fetchone(sql, value):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, value)
            fetch_result = cursor.fetchone()
    finally:
        connection.close()
    return fetch_result


def fetchall(sql, value):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, value)
            fetch_result = cursor.fetchall()
    finally:
        connection.close()
    return fetch_result
