# Smart Folder Duplicator

Project latihan Python untuk menduplikasi folder menggunakan:

- `pathlib`
- `shutil.copytree()`
- `while` loop

## Cara menjalankan

Masuk ke folder project:

```bash
cd smart_folder_duplicator
```

Lalu jalankan:

```bash
python main.py
```

Program akan menyalin:

```text
sample_project/
```

menjadi:

```text
sample_project_copy/
```

Jika `sample_project_copy/` sudah ada, program otomatis membuat:

```text
sample_project_copy_2/
sample_project_copy_3/
sample_project_copy_4/
```

dan seterusnya.

## Latihan

Coba ubah:

```python
source = Path("sample_project")
destination = Path("sample_project_copy")
```

menjadi nama folder lain.

Kemudian coba jalankan program beberapa kali dan lihat bagaimana nama folder tujuan berubah.
