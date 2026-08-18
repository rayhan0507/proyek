# Dead Folder Detector

Project Python sederhana untuk mencari folder kosong di dalam sebuah project.

## Library yang Digunakan

* `pathlib` — mencari dan mengecek folder.
* `shutil` — menghapus folder.
* `sys` — menerima input dari command line.

## Struktur Project

```text
dead-folder-detector/
├── main.py
├── README.md
└── sample_project/
    ├── src/
    │   └── app.py
    ├── docs/
    │   └── readme.txt
    ├── assets/
    ├── empty_folder/
    └── unused/
        └── temp/
```

`empty_folder` dan `unused/temp` sengaja dibuat kosong untuk pengujian.

## Cara Menjalankan

```bash
python main.py sample_project
```

Program akan mencari folder kosong secara recursive.

Contoh output:

```text
Scanning: sample_project

[DEAD] sample_project/assets
[DEAD] sample_project/empty_folder
[DEAD] sample_project/unused/temp

Found 3 dead folders.
```

## Menghapus Folder

Gunakan `--delete` jika ingin menghapus folder yang ditemukan:

```bash
python main.py sample_project --delete
```

Program akan meminta konfirmasi sebelum menghapus:

```text
Found 3 dead folders.

Delete them? (y/n): y

Folders deleted successfully.
```

## Tantangan

Program harus bisa:

1. Mencari folder secara recursive.
2. Mendeteksi folder yang kosong.
3. Menampilkan semua folder yang ditemukan.
4. Menerima path dari `sys.argv`.
5. Menghapus folder menggunakan `shutil` jika menggunakan `--delete`.

## Tujuan

Project ini dibuat untuk latihan:

* `pathlib`
* `shutil`
* `sys.argv`
* recursive folder scanning
* operasi file dan folder dengan Python
