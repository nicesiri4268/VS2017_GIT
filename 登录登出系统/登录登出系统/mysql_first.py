import mysql.connector
import sys


try:
    cnx = mysql.connector.connect( user='zhu' , password= 'zhu135335',
                              host = '127.0.0.1' ,)
except: 
    print ("数据库连接异常!")
    sys.exit(-1)

#x=cnx.ping(reconnect= False,attempts=1, delay=0 )
#print (x)
#x=cnx.reconnect(attempts= 1 ,delay = 1)
#print (x)
x= cnx.is_connected()#当mysql连接可用时返回true,可以用于检测连接是否成功
print (x)
cursor = cnx.cursor()

cursor.execute('use first')
#选择first数据库
#execute("")是用来输入sql语句的命令
cursor.execute('select * from math')#输出math的全部的行

print (cursor.fetchall())

cnx.close() #关闭mysql的连接