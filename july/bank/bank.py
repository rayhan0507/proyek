from abc import ABC, abstractmethod
from mariadb_bank import conn


class EntitasBank(ABC):
    """Kelas abstrak: aturan bahwa setiap entitas bank wajib bisa disimpan ke DB."""

    @abstractmethod
    def simpan(self):
        """Wajib diimplementasikan oleh subclass untuk menyimpan data ke database."""
        pass


class Bank(EntitasBank):
    """Kelas dasar berisi data identitas pengguna bank."""

    def __init__(self, nama, password, alamat, no_hp):
        self.nama = nama
        self.password = password
        self.alamat = alamat
        self.no_hp = no_hp

    # def cari_rekening():
    # def tampilkan_semua():


class Nasabah(Bank):
    def __init__(self, nama, password, alamat, no_hp):
        super().__init__(nama, password, alamat, no_hp)

    def simpan(self):
        cur = conn.cursor()
        sql = """
            INSERT INTO nasabah(nama, alamat, no_hp, password_user)
            VALUES(?, ?, ?, ?)
        """
        data = (self.nama, self.alamat, self.no_hp, self.password)
        cur.execute(sql, data)
        conn.commit()

    def buat_akun(self):
        self.simpan()


class Rekening(EntitasBank):

    def __init__(self, nama_nasabah, no_rekening, jenis_rekening,
                 rekening_keaktifan=True, saldo_awal=0):
        self.nama_nasabah = nama_nasabah
        self.no_rekening = no_rekening
        self.jenis_rekening = jenis_rekening
        self.rekening_keaktifan = rekening_keaktifan
        self.saldo_awal = saldo_awal

    def simpan(self):
        cur = conn.cursor()
        sql = """
            INSERT INTO rekening(no_rekening, jenis_rekening, saldo, nama_nasabah, rekening_keaktifan)
            VALUES(?, ?, ?, ?, ?)
        """
        data = (self.no_rekening, self.jenis_rekening, self.saldo_awal,
                self.nama_nasabah, self.rekening_keaktifan)
        cur.execute(sql, data)
        conn.commit()

    def buat_rekening(self):
        self.simpan()


# class transaksi:


def main():
    inp = 0
    print("===== Login =====")
    user = input("username: ")
    pw = input("password: ")
    alamat = input("alamat: ")
    no_hp = input("nomor hp: ")
    nasabah = Nasabah(user, pw, alamat, no_hp)
    nasabah.buat_akun()

    while inp != "7":
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
        inp = input("pilih: ").strip()

        if inp == "1":
            no_rekening = input("buat nomor rekening: ")
            saldo_awal = 0
            jenis_rekening = input("jenis_rekening (Tabungan/Giro) :")
            rekening_keaktifan = True
            r = Rekening(user, no_rekening, jenis_rekening, rekening_keaktifan, saldo_awal)
            r.buat_rekening()
            print(f"Rekening {no_rekening} berhasil dibuat.")


if __name__ == "__main__":
    main()