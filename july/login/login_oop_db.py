import mariadb 
from config import DB_USER, DB_HOST, DB_PASSWORD, DB_PORT, DB_NAME
try: 
    conn = mariadb.connect(
        user=DB_USER,
        host=DB_HOST,
        password=DB_PASSWORD,
        port=DB_PORT,
        database=DB_NAME
    )   

    cur = conn.cursor()


    def check_data(user, password) -> bool:
        cur.execute("SELECT * FROM pengguna")
        hasil = cur.fetchall()
        for idUser, username, password_user in hasil:
            if username == user and password_user == password:
                return True
        return False


    def add_data(user, password):
        sql = f"""
        INSERT INTO pengguna
        (username, password_user)
        VALUES (?, ?)
        """

        data = (user, password)
        cur.execute(sql, data)
        conn.commit()

except mariadb.Error as e:
    print(f"Error: {e}")