CREATE DATABASE IF NOT EXISTS sistem_bank;

CREATE TABLE if not EXISTS nasabah(
    id_nasabah INT AUTO_INCREMENT,
    nama VARCHAR(50),
    alamat VARCHAR(50),
    no_hp INT,
    password_user VARCHAR(50),

    PRIMARY KEY(id_nasabah)
);

CREATE TABLE if not EXISTS rekening(
    id_nasabah INT,
    no_rekening INT,
    jenis_rekening VARCHAR(50),
    saldo INT,

    PRIMARY KEY (no_rekening),
    FOREIGN KEY (id_nasabah) REFERENCES nasabah(id_nasabah)
);

CREATE TABLE if not EXISTS transaksi(
    id_transaksi INT PRIMARY KEY,
    no_rekening INT,
    jenis VARCHAR(50),
    nominal INT,
    tanggal DATE,
    PRIMARY KEY (id_transaksi),
    FOREIGN KEY (no_rekening) REFERENCES rekening(no_rekening)

);

