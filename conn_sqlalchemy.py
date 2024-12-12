from sqlalchemy import create_engine

def get_sqlalchemy_conn():
    """
    Devuelve una conexión SQLAlchemy a la base de datos.
    """
    server = '192.168.3.106'
    database = 'automatizacion'
    username = 'dba_test'
    password = 'Report$51'

    # Crear cadena de conexión
    connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    return create_engine(connection_string)
