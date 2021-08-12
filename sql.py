
import mysql.connector as m
import pandas as pd
import numpy as np

mydb = m.connect(
  host="localhost",
  user="root",
  password="thari",database="project")
mycursor = mydb.cursor()

df = pd.read_csv('test.csv', index_col=False)
df = df.fillna(0)

column_names = df.columns.tolist()
#column_names_tup =tuple(column_names)
def table_create(list):
    default = 'CREATE TABLE students ('
    for i in list:
        if i == 'name' :
            default = default + str(i) + ' VARCHAR(255),'
        else:
            default = default + str(i) + ' int,'
    string = default + ")"
    return string
column = table_create(column_names)

mycursor.execute(column)

def table_create(list):
    default = 'CREATE TABLE students ('
    for i in list:
        if i == 'name' :
            default = default + str(i) + ' VARCHAR(255),'
        else:
            default = default + str(i) + ' int,'
    string = default + ")"
    return string
    #print(string)
column = table_create(column_names)

def table_insert(list, row_numbers):
    default = 'INSERT INTO students VALUES '
    df = pd.read_csv('test.csv', index_col=False)
    df = df.fillna(0)
    #values = df[df.index.isin([row_numbers])]
    values = df.iloc[row_numbers].tolist()
    values = tuple(values)
    #del values[0]
    default = default + str(values)
    string = default + ''
    return string

forrows = table_insert(column_names, 1)
insert = table_create(column_names)

#print(forrows)
# print(column_names)

def for_loop_rows(data):
    df = pd.read_csv('test.csv', index_col=False)
    df = df.fillna(0)
    length = len(df.index)
    for i in range(0,length):
        forrows = table_insert(column_names, i)
        mycursor.execute(forrows)
        print(forrows)
for_loop_rows('data')
