# web-mysql
**A pure Python mysql connect tool which base on PyMysql**

**A toolkit that simplifies the operation of Python website connecting to Mysql database.
Just set database settings and you can fetchone,fetchall,executor function to operate mysql database in Python3.**

use pip to install this package:
`pip3 install web-mysql`

You can input sql command string and values list like this:
```Python
sql = "insert into users (name,age) values (%s,%s);"
values = ['your_name',11]
```
Than these function will use pymysql to execute the sql command to oprate mysql database.

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


2020/1/24
---
1.0.0.dev

**register this package. Develop version.**
