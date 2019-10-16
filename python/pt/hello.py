
import mysql.connector

i =10
print(i)

import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="",   # 数据库密码
  database="runoob_db",
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE runoob_db")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
# print(mydb)
#mycursor.execute("CREATE TABLE sites(name VARCHAR(255),url VARCHAR(255))")
#mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

#插入数据
# sql = "INSERT INTO sites(name,url) VALUES (%s,%s)"
# val = ("RUNOOB","https://www.runoob.com")
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"记录插入成功")

#批量插入
# sql = "INSERT INTO sites(name,url) VALUES(%s,%s)"
# val =[
#   ('Google', 'https://www.google.com'),
#   ('Github', 'https://www.github.com'),
#   ('Taobao', 'https://www.taobao.com'),
#   ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"记录插入成功")

#print(mycursor.lastrowid)

#查询
# sql = "select * from sites"
# sql = "select * from sites where name = 'RUNOOB'"
# sql = "select * from sites where url like '%oo%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall() #fetchall获取所有记录  fetchone #第一条记录
# for x in myresult:
#   print(x)

# sql = "select * from sites where name = %s"
# val = ("RUNOOB",)
# mycursor.execute(sql,val)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

#删
# sql = "delete from sites where name='stackoverflow'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount," 条记录删除")

#改
# sql = "update sites set name='tb' where name='Taobao'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,'条记录修改')

# sql = "drop table if exists sites"
# mycursor.execute(sql)
