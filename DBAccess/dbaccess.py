import pyodbc
import pandas as pd

def get_db_connection():
    driver = r'{ODBC Driver 13 for SQL Server}'
    server = r'ARC-PC-0242\SQLEXPRESS2014'
    database = r'tanida_test'
    uid = r'sa'
    pwd = r'root00++'

    ret = pyodbc.connect(
    'DRIVER=' + driver + ';'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + uid + ';'
    'PWD=' + pwd
    )

    return ret

def sp_execute(sp_name, param):
    con = get_db_connection()

    sql = 'exec' + '\n'
    sql += sp_name + '\n'

    for key, value in param.items():
        val = str(value) if value is not None else 'NULL'
        sql += '%s = %s ,' % (str(key), val)
    else:
        sql = sql[:-1]

    ret = pd.read_sql(
    sql,
    con,
    )
    # 返却テーブルの行列変換
    ret = ret.T
    return ret
