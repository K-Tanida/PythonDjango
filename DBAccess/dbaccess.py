import pyodbc
import numpy as np
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
    ret =[]
    con = get_db_connection()
    cur = con.cursor()

    # SQL作成
    sql = 'exec' + '\n'
    sql += sp_name + '\n'
    for key, value in param.items():
        val = str(value) if value is not None else 'NULL'
        sql += '%s = %s ,' % (str(key), val)
    else:
        sql = sql[:-1]

    # SQL実行
    cur.execute(sql)

    # 返却されたデータセットをループ
    while True:
            desc = cur.description
            rows = cur.fetchall()
            array = np.array(rows)
            df = pd.DataFrame(array)
            # インデックス名変更
            columns = []
            for columnIndex in range(0,len(desc)):
                columns.append(desc[columnIndex][0])
            else:
                df.columns = columns

            ret.append(df.T)
            if not cur.nextset():
                break
    cur.close()
    con.close()
    return ret
