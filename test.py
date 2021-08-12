import mysql.connector as m
import pandas as pd
from datetime import date
import numpy as np
# mydb = m.connect(
#   host="localhost",
#   user="root",
#   password="thari",database="project")
# mycursor = mydb.cursor()
# #mycursor.execute('CREATE TABLE studen (name VARCHAR(255),`25/02/2021` int,`26/02/2021` int,`27/02/2021` int,`28/02/2021` int,`29/02/2021` int,`30/02/2021` int,`31/02/2021` int);')
#
# sql = "INSERT INTO student (name, `25/02/2021`, `26/02/2021`, `27/02/2021`, `28/02/2021`, `29/02/2021`,`30/02/2021`,`31/02/2021`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# val = [
#   ('Peter', 1,0,1,0,1,1,0),
#   ('Amy', 1,0,1,0,0,1,0)
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")
#a=mycursor.fetchall()
#print(a)
# 'CREATE TABLE student (name VARCHAR(255),`25/02/2021` int,`26/02/2021`
# int,`27/02/2021` int,`28/02/2021` int,`29/02/2021` int,`30/02/2021` int,
# `31/02/2021` int);'

# sql = "INSERT INTO student (name, `25/02/2021`, `26/02/2021`, `27/02/2021`, `28/02/2021`, `29/02/2021`,`30/02/2021`,`31/02/2021`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# val = [
#   ('Peter', 1,0,1,0,1,1,0),
#   ('Amy', 1,0,1,0,0,1,0)
# ]

def table_creation(df):
    #today = str(date.today())
    #print(today)
    default = 'CREATE TABLE student (name VARCHAR(255),`'
    #print(df)
    column_names = df.columns.tolist()
    #print(column_names)
    for i in column_names:
        if i == 'name' :
            pass
        else:
            default = default + str(i) + '` int,`'
    default = default[:-2]
    default = default + ');'
    return default
    #print(default)

# sql = "INSERT INTO student (name, `25/02/2021`, `26/02/2021`, `27/02/2021`,
#`28/02/2021`, `29/02/2021`,`30/02/2021`,`31/02/2021`)
#VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# val = [
#   ('Peter', 1,0,1,0,1,1,0),
#   ('Amy', 1,0,1,0,0,1,0)
# ]
def to_executemany(df):
     default = 'INSERT INTO student (name,`'
     column_names = df.columns.tolist()
     for i in column_names:
         if i == 'name' :
             pass
         else:
             default = default + str(i) + '`,`'
     default = default[:-2]
     default = default + ') VALUES ('
     for i in range(len(column_names)):
         default = default+'%s,'
     default = default[:-1]
     default = default + ')'
     return default
    # print (default)

def to_values(df):
    records = df.to_records(index=False)
    result = list(records)
    revalue = []
    for a in result:
        retuple = []
        for i in a:
            #print(type(i))
            if type(i) == str:
                retuple.append(i)
            elif type(i) == np.float64:
                retuple.append(int(i))
            elif type(i) == np.int64:
                retuple.append(int(i))
        #print(retuple)
        revalue.append(tuple(retuple))

    # for a in result:
    #     int(str(a).replace('.', ''))
    #     print(a)
    #int(str(result).replace('.', ''))
    #print(result)
    #print(revalue)

    #print(result)
    # for a in result:
    #     #print(a)
    #     for  n, i in enumerate(a):
    #         #print(i)
    #         if i == 1.:
    #             a[n] = int(1)
    #         elif i == 0.:
    #             a[n] = int(0)
    #         else:
    #             a[n] = i
    #     print(a)
    # #print(a)

    return revalue

    #print(result)

def for_sql(self):
    mydb = m.connect(host="localhost",user="root",password="thari",database="project")
    mycursor = mydb.cursor()
    sql = "DROP TABLE IF EXISTS student"
    df = pd.read_csv('test.csv', index_col=False)
    df = df.fillna(0)
    mycursor.execute(sql)
    create = table_creation(df)
    #mycursor.execute('CREATE TABLE student (name VARCHAR(255),`25/02/2021` int,`26/02/2021` int,`27/02/2021` int,`28/02/2021` int,`29/02/2021` int,`30/02/2021` int,`31/02/2021` int);')
    mycursor.execute(create)
    sql =to_executemany(df)
    to_values(df)
    #sql = "INSERT INTO student (name, `25/02/2021`, `26/02/2021`, `27/02/2021`, `28/02/2021`, `29/02/2021`,`30/02/2021`,`31/02/2021`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    # val = [
    #   ('Peter', 1,0,1,0,1,1,0),
    #   ('Amy', 1,0,1,0,0,1,0)
    # ]
    #to_executemany(df)
    val =to_values(df)
    print(val)
    mycursor.executemany(sql, val)

    mydb.commit()




for_sql('hi')
