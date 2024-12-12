from conn_sqlalchemy import get_sqlalchemy_conn


def export_dataframe_to_sql(df, table_name, schema='omni', if_exists='replace'):
    """
    Exporta un DataFrame a una tabla en SQL Server.

    Parámetros:
        - df: DataFrame de pandas.
        - table_name: Nombre de la tabla en SQL Server.
        - if_exists: Comportamiento si la tabla ya existe ('replace', 'append', 'fail').
    """
    # Obtén la conexión desde `db_connection.py`
    engine = get_sqlalchemy_conn()

    try:
        df.to_sql(table_name, con=engine, schema=schema, if_exists=if_exists, index=False)
        print(f"Datos exportados exitosamente a la tabla '{table_name}'.")
    except Exception as e:
        print(f"Error al exportar los datos: {e}")
