
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

# sql = "INSERT INTO sites(name,url) VALUES (%s,%s)"
# val = ("RUNOOB","https://www.runoob.com")
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"记录插入成功")
