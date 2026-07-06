from bank_cfg import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT

import mariadb

try:
    conn = mariadb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )


except mariadb.Error as e:
    print(f"Error {e}")