import pyodbc
def get_sqlserver_connection():
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=192.168.3.106;'
        r'DATABASE=automatizacion;'
        r'UID=dba_test;'
        r'PWD=Report$51'
    )
    return pyodbc.connect(conn_str)

