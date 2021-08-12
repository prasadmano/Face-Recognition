import os, time, csv
import pandas as pd
from datetime import date
import numpy as np

#dataframe to check the column

def for_col(self):
    today = str(date.today())
    #print(today)
    df = pd.read_csv('test.csv')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    #print(df)
    dates = list(df)
    #print(dates[-1])
    if dates[-1] == today:
        #print('in if')
        pass
    else:
        #print('in else')
        df[today] = np.nan
        #print(df)
        df.to_csv('test.csv', index=False)


#for_col('testdatabase')

# dataframe names ask_update

def for_names(name_update):
    df = pd.read_csv('test.csv', index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    print(df)
    #print(df)
    #name_list = df.iloc[0:50,0:1]
    name_list = df['name'].tolist()
    print(name_list)
    name_list_dup = name_list
    #name_listoflist = name_list.values.tolist()
    #name_listoflist = name_list
    #name_flat_list = [item for sublist in name_listoflist for item in sublist]
    #print(name_flat_list)
    for name in name_list:
        print(name)
        if name == name_update:
            n = 1
            #print('in if')
        else:
            n = 0
    if n == 0:
        name_list_dup.append(name_update)
        print(name_list_dup)
        with open('test.csv','a+', newline='') as f:
            wr = csv.writer(f, dialect='excel')
            a = [name_update]
            wr.writerow(a)

        print(df)

        # name_list_dup.append(name_update)
        # df.drop('name', axis=1)
        # print(df)
        # print(name_update)
        # df['name'] = name_list_dup
        # df.set_index('name')
        # #print(df)
        # df.to_csv('test.csv', index=False)

#for_names('prassss')

# to assign present or absent

def csv_registering(present_name):
    today = str(date.today())
    df = pd.read_csv('test.csv', index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.at[(df['name'] == present_name), today] = 1
    df.to_csv('test.csv', index=False)

#csv_registering('saranya')






def for_date(path):
    # folder = os.listdir(path)
    # print(folder)
    # #list2 = []
    # df = pd.read_csv('test.csv')
    # #print(df.iloc[0:50,0:1])
    # name_list = df.iloc[1:50,0:1]
    # #print(df.values.tolist())
    # name_listoflist = name_list.values.tolist()
    # name_flat_list = [item for sublist in name_listoflist for item in sublist]
    # print(name_flat_list)
    # df.at['prasad', 'x'] = 10
    # print(df)
    today = date.today()
    print(today)
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            break
    if row[-1] == today:
        pass

    else:
        file.close()
        with open('test.csv','w') as wfile:
            wr = csv.writer(wfile, dialect='excel')
            a = ['test']
            wr.writerow(a)





    # date list
    # date_list = df.iloc[0:1,1:50]
    # date_listoflist = date_list.values.tolist()
    # date_flat_list = [item for sublist in date_listoflist for item in sublist]
    # print(date_flat_list)

    #my_data = genfromtxt('test.csv', delimiter=',')
    #print(my_data)
    # with open('test.csv','a+', newline='') as f:
    #     wr = csv.writer(f, dialect='excel')
    #     a = ['test']
    #     wr.writerow(a)

#for_date('testdatabase')

# from sqlalchemy import create_engine
#
# dataset = pd.read_csv('test.csv', index_col=False)
#
# engine = create_engine('sqlite://',
#                        echo = False)
#
#
# dataset.to_sql('Employee_Data',
#                con = engine)
#
# print(engine.execute("SELECT * FROM Employee_Data").fetchall())


import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv ('test.csv')   
df = pd.DataFrame(data, columns= ['Name','Country','Age'])

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('CREATE TABLE people_info (Name nvarchar(50), Country nvarchar(50), Age int)')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO TestDB.dbo.people_info (Name, Country, Age)
                VALUES (?,?,?)
                ''',
                row.Name,
                row.Country,
                row.Age
                )
conn.commit()
