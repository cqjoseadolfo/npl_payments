import pyodbc
def get_sqlserver_connection():
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-ANGIACE\MSSQLSERVER2022;'
        r'DATABASE=servex;'
        r'UID=cqjoseadolfo;'
        r'PWD=Report$51.'
    )
    return pyodbc.connect(conn_str)

