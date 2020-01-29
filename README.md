
# Web-MySQL
A pure Python MySQL connect tool which base on PyMySQL

A toolkit that simplifies the operation of Python website connecting to MySQL database.
Just set MySQL settings and you can fetchone,fetchall,executor function to operate MySQL database in Python3..

use pip to install this package:
`pip3 install Web-MySQL`

use pip to upgrade Web-MySQL:
`pip3 install --upgrade Web-MySQL`

You can input sql command string and values list which format is as follows:
```Python
sql = "insert into users (name,age) values (%s,%s);"
values = ['your_name',11]
```
Than these function will use PyMySQL to execute the sql command to oprate MySQL database.

```Python
# executor function only execute the sql command and it will not return anything.
def executor(sql,values):
  ...
 
# fetchone function will execute the select sql command and fetch the first select result.
def fetchone(sql,values):
 ...
 return fetch_result

# fetchall function will execute the select sql command and fetch all select result as list.
def fetchall(sql,values):
  ...
  return fetch_result
```

We can configure the database and use the recommended usage to use functions as follows.

Create a golbal Connector instance, and modify the corresponding variables which are database connection information;

```Python
from web_mysql import Connector

connector = Connector()
connector.host = "localhost"
connector.user = "root"
connector.password = "123456"
connector.database = "test"

def insert_user():
  sql = "insert into users (name,id) values (%s,%s);“
  values = ["name", 10001]
  connector.executor(sql, values)

def get_user(name, id):
  sql = "select * from users where name=%s and id=%s;"
  values = [name, id]
  user = connector.fetchone(sql, values)

def get_users():
  sql = "select * from users;"
  all_user = connector.fetchall(sql)
```

1.0.0
---

2020/1/29  正式发布
