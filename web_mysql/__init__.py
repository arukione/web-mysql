"""
Web-MySQL: A pure-Python MySQl tool which base on PyMySQL

Copyright (c) 2020 Web-MySQL contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# Please see the LICENSE of all open source libraries in QUOTE file.
# https://github.com/arukione/Web-MySQL

# Use pure-Python MySQL client library PyMySQL
# https://github.com/PyMySQL/PyMySQL
import pymysql


class Connector:

    def __init__(self):
        """
        MySQL connector parameters init.
        """
        self.host = "localhost"
        self.user = "root"
        self.password = None
        self.database = None
        self.charset = 'utf8mb4',
        self.cursorClass = pymysql.cursors.DictCursor

    def connect(self):
        """
        A connection creation function.
        :return: mysql connection
        """
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.database,
            charset=self.charset,
            cursorclass=self.cursorClass
        )

    def executor(self, sql, values=None):
        """
        Executor mysql sql command.
        :param sql: The mysql command
        :param values: Parameter values for the mysql command
        :return: Don't return anything
        """
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, values)
        finally:
            connection.commit()
            connection.close()

    def fetchone(self, sql, value=None):
        """
        Execute mysql select command and return a cursor fetchone result.
        :param sql: The mysql command
        :param value: Parameter values for the mysql command
        :return: cursor.fetchone()
        """
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, value)
                fetch_result = cursor.fetchone()
        finally:
            connection.close()
        return fetch_result

    def fetchall(self, sql, value=None):
        """
        Execute mysql select command and return cursor fetchall result.
        :param sql: The mysql command
        :param value: Parameter values for the mysql command
        :return: cursor.fetchall()
        """
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, value)
                fetch_result = cursor.fetchall()
        finally:
            connection.close()
        return fetch_result
