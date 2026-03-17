import pymssql
import random
import time

server="k94701210.database.windows.net"
database="free-sql-db-2916645"
user="dbeng2"
password="Ab123456"

connect = pymssql.connect(server,user,password,database)