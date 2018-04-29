# …or push an existing repository from the command line
# git remote add origin https://github.com/nvetrov/MSSQL.git
# git push -u origin master
import pyodbc
server = 'tcp:prs043'
database = 'OST'
username = 'sa'
password = 'russi@'
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor()
cursor.execute("select TOP 100 BAR_CODE, LM_CODE, CAPTION  FROM [dbo].[Scenter]")
i = 0
for c in cursor:
    i += 1
    print(i, c.BAR_CODE, c.LM_CODE, c.CAPTION)

cursor.close()
connection.close()

