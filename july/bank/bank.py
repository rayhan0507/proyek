from mariadb_bank import conn

class Bank:
    def __init__(self, nama, password, alamat, no_hp):
        self.nama = nama
        self.password = password
        self.alamat = alamat
        self.no_hp = no_hp

    def tambah_nasabah(self, nama, password, alamat, no_hp):
        cur = conn.cursor()

        sql = """
            INSERT INTO nasabah(nama, alamat, no_hp, password_user)
            VALUES(?, ?, ?, ?)
        """

        data = (nama, alamat, no_hp, password)
        cur.execute(sql, data)
        conn.commit()

    # def buat_rekening():

    # def cari_rekening():

    # def tampilkan_semua():


class Nasabah(Bank):
    def __init__(self, nama, password, alamat, no_hp):
        super().__init__(nama, password, alamat, no_hp)
        self.nama = nama
        self.password = password
        self.alamat = alamat
        self.no_hp = no_hp

    @property
    def buat_akun(self):
        b = Bank(self.nama, self.password, self.alamat, self.no_hp)
        b.tambah_nasabah(self.nama, self.password, self.alamat, self.no_hp)

# class Rekening:

# class transaksi:


def main():
    inp = 0
    print("===== Login =====")
    user = input("username: ")
    pw = input("password: ")
    alamat = input("alamat: ")
    no_hp = int(input("nomor hp: "))
    nasabah = Nasabah(user, pw, alamat, no_hp)
    nasabah.buat_akun

    while inp != 7:
        print("===== BANK RYXA =====")
        print("""
            1. Buat Rekening
            2. Setor Uang
            3. Tarik Uang
            4. Transfer
            5. Lihat saldo
            6. Semua Rekening
            7. Keluar
        """)
        inp = int(input("pilih: "))
        

if __name__ == "__main__":
    main()