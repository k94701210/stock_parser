import pymssql

server="k94701210.database.windows.net"
database="free-sql-db-2916645"
user="dbeng2"
password="Ab123456"

connect = pymssql.connect(server,user,password,database)
print("登入成功")

cursor=connect.cursor()

print("cursor取得成功")

cursor.execute("select * from 練習的stock")

record=cursor.fetchall()

rec_count=len(record)

print(f"總共查到了{rec_count}筆資料")