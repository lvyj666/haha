import pymysql
db_config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'db':'test'   #数据库
}
# \ **db_config

conn = pymysql.connect(**db_config)
#建立游标（只有建立了游标才能操作数据库数据）
cursor1 = conn.cursor()  #实例化
#执行语句
#excute('sql语句')是执行语句的方法
#在pymysql中执行SQL语句不用加；号
cursor1.execute('show tables')
#获取数据集(列表)-->此处需要主动获取数据。
# cursor1.execute("")
values = cursor1.fetchall()
#打印数据
for value in values:
    print(value)lvyoujunstudy666
#提交--->把数据保存到磁盘中去
conn.commit()
#游标关闭
cursor1.close()
#连接关闭
conn.close()

if  __name__ == '__main__':




