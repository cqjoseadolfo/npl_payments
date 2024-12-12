from conn_pyodbc import get_sqlserver_connection

def get_cuenta_npl(contrato_param):
    """
    Obtiene la cuenta asociada al número de contrato servex proporcionado.
    """
    conn = get_sqlserver_connection()
    cursor = conn.cursor()

    query = """
        SELECT cuenta
        FROM [servex].[omni].[vw_cuentas_activas_npl]
        WHERE CONTRATO_CAJAS = ? OR CONTRATO_IBK = ?
    """
    cursor.execute(query, (contrato_param,contrato_param))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None