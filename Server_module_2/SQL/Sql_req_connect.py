import pyodbc
def sqlsr(IDgetsr):
    conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-E2PGTAG\SQLEXPRESS2019; Database=SQLDB; UID=dh; PWD=31052001')
    IDss = str(IDgetsr)
    IDss = "'" + IDss + "'"
    cursor = conx.cursor()
    select = "select * from dboData where ID = " + IDss + " AND Status = 'Done'"
    cus = cursor.execute(select)
    for row in cus:
        print(str(row)) 
    conx.close()
    return row