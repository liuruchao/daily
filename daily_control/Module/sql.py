#coding=utf-8

# import mysql.connector
# 封装增、删、查功能

def select(mydb,table,condition,flied='*'):
    mycursor = mydb.cursor(dictionary=True)
    val = (flied,table,condition)
    sql = 'select %s from %s  %s' % val
    # print(sql)
    mycursor.execute(sql)
    res = mycursor.fetchall()
    mycursor.close()
    # mydb.close()
    return res


def insert(mydb,table,**fields):
    mycursor = mydb.cursor(dictionary=True)
    field = ''
    val = []
    for key in fields:
        field =  field  + key + ','
        val.append(fields[key])
    field = field[:-1]    
    val = str(tuple(val))
    sql = "INSERT INTO "+ table + "(" + field +") VALUES " + val  
    # print(sql)
    mycursor.execute(sql)
    mycursor.close()
    mydb.commit()    # 数据表内容有更新，必须使用到该语句
    return [mycursor.rowcount,mycursor.lastrowid]

def delete(mydb,table,where):
    mycursor = mydb.cursor(dictionary=True)
    val = (table,where)
    sql = 'DELETE FROM %s WHERE %s' % val
    mycursor.execute(sql)
    mycursor.close()
    mydb.commit()
    return mycursor.rowcount

