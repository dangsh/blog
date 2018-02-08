#!/usr/bin/python
#-*-coding:utf-8 -*-
import pymysql.cursors
 
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'5801200zxg',
          'db':'blog',
          'cursorclass':pymysql.cursors.DictCursor,
          'charset':'utf8'
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

    except:
        print("add error")

def msgDel(id):
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = 'DELETE FROM blog1 where id = ' + id
            cursor.execute(sql);
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()

    except:
        print("add error")

def msgSelect(page):
    allUsertables = []
    try:
        with connection.cursor() as cursor:
            sql = 'select id , title , shortmsg , msg from blog1 limit '+ str((int(page)-1)*10) +',10'
            cursor.execute(sql);
            for row in cursor.fetchall():
                allUsertables.append(row)
        connection.commit()
    except:
        print("select error")
    return allUsertables

def msgPageSelect():
    num = 0
    try:
        with connection.cursor() as cursor:
            sql = 'select count("id") from blog1'
            cursor.execute(sql);
            page = cursor.fetchall()
            for k,v in page[0].items():
                num = v
        connection.commit()
    except:
        print("select error")
    return num
    

def oneSelect(id):
    allUsertables = []
    try:
        with connection.cursor() as cursor:
            sql = 'select id , title , shortmsg , msg from blog1 where id =' + id
            cursor.execute(sql);
            for row in cursor.fetchall():
                allUsertables.append(row)
        connection.commit()
    except:
        print("select  one  error")
    return allUsertables

if __name__ == "__main__":
    msgPageSelect()