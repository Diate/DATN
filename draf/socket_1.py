import pyodbc


print(pyodbc.drivers())

conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-E2PGTAG\SQLEXPRESS2019; Database=SQLDB; UID=dh; PWD=31052001')

cursor = conx.cursor()

name = "'IUYX8635'"
select = "select * from dboData where ID = " + name
for row in cursor.execute(select):
    # print(row.ProductID)
    # print(row[0])
    customer_list = dict(enumerate(item[0] for item in select))
    print(row)
    print(str(row))
    print(type(str(row)))
    print(type(row))
    # print(customer_list)
    # print(type(customer_list))
#cursor.execute("select * from Products")

#data = cursor.fetchall()

#print(data)

conx.close()