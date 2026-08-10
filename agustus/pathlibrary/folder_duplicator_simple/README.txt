SOAL: FOLDER DUPLICATOR

Tugas:
Buat program yang menyalin folder "source" menjadi folder "backup".

Sebelum:
    source/
    ├── hello.txt
    └── data.txt

Setelah program dijalankan:
    source/
    ├── hello.txt
    └── data.txt

    backup/
    ├── hello.txt
    └── data.txt

Wajib menggunakan:
    from pathlib import Path
    from shutil import copytree

Tidak perlu:
- validasi
- rglob
- input user
- error handling
- fitur tambahan

Fokus hanya memahami:
    Path()
    copytree()
    source
    destination
