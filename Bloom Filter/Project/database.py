import pyodbc
# con = pyodbc.connect('Trusted_Connection = yes', driver = 'ODBC Driver 17 for SQL Server',server = 'localhost\SQLEXPRESS', database = 'mydb')
con = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=localhost\SQLEXPRESS;'
    r'DATABASE=Article;'
    r'Trusted_Connection=yes;'
    r'autocommit=True;'
)
cursor = con.cursor()
# cursor.execute("select * from Article")


cursor.execute("INSERT INTO Article ([Name],Author) VALUES ('Butt','B')")
con.commit()  # Using this to update the values in database otherwise it wont work



# result = cursor.fetchall()
# for row in result:
#   print(row)