import pymysql.cursors
 
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'5801200zxg',
          'db':'blog',
          'cursorclass':pymysql.cursors.DictCursor,
          }
 
# Connect to the database
connection = pymysql.connect(**config)

def msgAdd(a , b , c):
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = 'INSERT INTO blog1 (title , shortmsg , msg) VALUES (%s, %s, %s)'
            cursor.execute(sql, (a , b , c));
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();

def msgSelect():
    allUsertables = []
    try:
        with connection.cursor() as cursor:
            sql = 'select title , shortmsg , msg from blog1'
            cursor.execute(sql);
            for row in cursor.fetchall():
                allUsertables.append(row)
        connection.commit()
    except:
        print("select error")

    return allUsertables
    # finally:
    #     connection.close();
