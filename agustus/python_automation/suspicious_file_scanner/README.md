# Scanner File Mencurigakan (Versi Simpel)

Satu file script Python (`scan.py`), tanpa class/OOP, cuma pakai
fungsi biasa. Cocok buat belajar `pathlib` dan `shutil`.

## Struktur folder

```
simple_file_scanner/
├── scan.py          <- semua logikanya ada di sini, dibaca dari atas ke bawah
├── sample_data/      <- contoh file buat dites (sudah ada file "aman" & "mencurigakan")
└── README.md
```

## Cara pakai

```bash
python scan.py
```

Script ini otomatis akan:
1. Scan folder `sample_data/`
2. Tampilkan daftar file yang mencurigakan beserta alasannya
3. Tanya apakah mau dipindahkan ke folder `karantina/` (jawab `y` atau `n`)
4. Kalau `y`, folder karantina otomatis di-zip

## Isi `scan.py`, bagian per bagian

| Fungsi | Fungsinya apa |
|---|---|
| `cek_satu_file(file_path)` | Cek 1 file, kembalikan alasan kalau mencurigakan |
| `scan_folder(nama_folder)` | Telusuri semua file pakai `Path.rglob("*")`, panggil `cek_satu_file` satu-satu |
| `tampilkan_laporan(temuan)` | Cetak hasil ke layar |
| `karantina_file(temuan)` | Pindahkan file pakai `shutil.move()` |
| `zip_folder(folder)` | Bikin file `.zip` pakai `shutil.make_archive()` |

## 3 kategori yang dideteksi

1. **Tanpa ekstensi** -> `path.suffix == ""`
2. **Nama mencurigakan**
   - Ekstensi ganda: `invoice.pdf.exe`
   - Nama kayak hash acak: `a8f5f167f44f...exe`
   - Kata berbahaya di nama: `crack`, `keygen`, `payload`, dll
3. **Ukuran aneh**
   - File 0 byte
   - File `.exe` yang kekecilan (< 10 KB)

Mau nambah aturan sendiri? Tinggal edit daftar `KATA_BERBAHAYA`,
`EKSTENSI_EXECUTABLE`, atau `BATAS_EXE_KECIL_BYTE` di bagian atas
`scan.py` — nggak perlu ubah logika lainnya.
