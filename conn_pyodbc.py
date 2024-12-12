import pyodbc
import yaml

# Cargar configuración
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

db_config = config['database']

def get_sqlserver_connection():
    """
    Devuelve una conexión pyodbc a la base de datos utilizando parámetros configurados.
    """
    conn_str = (
        f"DRIVER={{{db_config['driver']}}};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']};"
    )
    return pyodbc.connect(conn_str)
