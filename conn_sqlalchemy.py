from sqlalchemy import create_engine
import yaml

# Cargar configuración
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

db_config = config['database']

def get_sqlalchemy_conn():
    """
    Devuelve una conexión SQLAlchemy a la base de datos utilizando parámetros configurados.
    """
    connection_string = (
        f"mssql+pyodbc://{db_config['username']}:{db_config['password']}"
        f"@{db_config['server']}/{db_config['database']}?driver={db_config['driver'].replace(' ', '+')}"
    )
    return create_engine(connection_string)
