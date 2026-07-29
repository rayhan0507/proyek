from abc import ABC, abstractmethod
from mariadb_bank import conn


class EntitasBank(ABC):
    """Kelas abstrak: aturan bahwa setiap entitas bank wajib bisa disimpan ke DB."""

    @abstractmethod
    def simpan(self):
        pass

class Transaksi(ABC):
    @abstractmethod
    def setor(self, jumlah):
        pass
    @abstractmethod
    def tarik(self, jumlah):
        pass

class Melihat(ABC):
    @abstractmethod
    def lihat(self, user):
        pass

class Bank(EntitasBank):
    """Kelas dasar berisi data identitas pengguna bank."""

    def __init__(self, nama, password, alamat, no_hp):
        self.nama = nama
        self.password = password
        self.alamat = alamat
        self.no_hp = no_hp

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


class Rekening(EntitasBank, Transaksi, Melihat):

    def __init__(self, nama_nasabah, no_rekening, jenis_rekening, rekening_keaktifan=True, saldo=0):
        self.nama_nasabah = nama_nasabah
        self.no_rekening = no_rekening
        self.jenis_rekening = jenis_rekening
        self.rekening_keaktifan = rekening_keaktifan
        self.saldo = saldo

    def simpan(self):
        cur = conn.cursor()
        sql = """
            INSERT INTO rekening(no_rekening, jenis_rekening, saldo, nama_nasabah, rekening_keaktifan)
            VALUES(?, ?, ?, ?, ?)
        """
        data = (self.no_rekening, self.jenis_rekening, self.saldo,
                self.nama_nasabah, self.rekening_keaktifan)
        cur.execute(sql, data)
        conn.commit()

    def setor(self, jumlah):
        cur = conn.cursor()
        sql = """
            UPDATE rekening
            SET saldo = saldo + ?
            WHERE no_rekening = ? 
        """
        data = (jumlah, self.no_rekening)
        cur.execute(sql, data)
        conn.commit()

    def tarik(self, jumlah):
        cur = conn.cursor()
        sql = """
            UPDATE rekening
            SET saldo = saldo - ?
            WHERE no_rekening = ?
        """

        data = (jumlah, self.no_rekening)
        cur.execute(sql, data)
        conn.commit()

    def lihat(self, user, no_rekening) -> int:
        cur = conn.cursor()
        cur.execute("SELECT nama_nasabah, no_rekening, saldo FROM rekening")
        data = cur.fetchall()

        for row in data:
            USER, rek, saldo = row
            if USER == user and int(rek) == int(no_rekening):
                return saldo
            


    def buat_rekening(self):
        self.simpan()
    def setor_saldo(self, jumlah):
        self.setor(jumlah)
    def tarik_saldo(self, jumlah):
        self.tarik(jumlah)
    def lihat_saldo(self, user, no_rekening) -> int:
        print("membuka rekening anda...")
        print(f"saldo anda: {self.lihat(user, no_rekening)}")


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

        elif inp == "2":
            no_rek_tujuan = input("no rekening: ")
            isi_saldo = int(input("isi saldo: "))
            r = Rekening(user, no_rek_tujuan, "", True, isi_saldo)
            r.setor_saldo(isi_saldo)
            print(f"Saldo rekening anda ditambahkan")

        elif inp == "3":
            no_rek_tujuan = input("no rekening: ")
            tarik_saldo = int(input("tarik saldo: "))   
            r = Rekening(user, no_rek_tujuan, "", True, tarik_saldo)
            r.tarik_saldo(tarik_saldo)
            print(f"Anda berhasil menarik saldo anda")

        elif inp == "5":
            no_rek_tujuan = input("no rekening: ")
            r = Rekening(user, no_rek_tujuan, "", True, 0)
            r.lihat_saldo(user, no_rek_tujuan)
            


if __name__ == "__main__":
    main()