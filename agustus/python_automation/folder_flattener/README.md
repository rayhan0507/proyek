# Folder Flattener

Simple Python automation project for collecting files from nested folders into a single `flattened` directory.

## Description

Folder Flattener scans the current working directory recursively with `pathlib.Path.rglob()`. Every file it finds, except `main.py`, is checked before being moved into the `flattened` directory using `shutil.move()`.

The project also checks whether a file with the same name already exists in `flattened`. If a duplicate is found, that file is skipped instead of being moved.

## Example

### Before

```text
folder_flattener_test/
├── Documents/
│   ├── tugas.pdf
│   └── Kuliah/
│       └── alpro.py
├── Pictures/
│   └── foto.jpg
├── flattened/
└── main.py
```

### After

```text
folder_flattener_test/
├── Documents/
├── Pictures/
├── flattened/
│   ├── tugas.pdf
│   ├── alpro.py
│   └── foto.jpg
└── main.py
```

## Features

- Recursively scans files using `Path.rglob("*")`.
- Ignores `main.py`.
- Moves files with `shutil.move()`.
- Checks for duplicate filenames before moving.
- Keeps the first file when a duplicate filename is found and skips the next one.

## Libraries Used

Only Python standard-library modules are used:

- `pathlib` — path handling and recursive file scanning.
- `shutil` — moving files.
- `abc` — defining the abstract interface.

## Project Structure

```text
folder_flattener_test/
├── main.py
├── README.md
├── flattened/
├── Documents/
├── Pictures/
└── Projects/
```

## How It Works

The program follows this flow:

```text
Start
  ↓
Get current working directory
  ↓
Scan recursively with rglob("*")
  ↓
Is it a file?
  ↓ Yes
Is it main.py?
  ↓ No
Check duplicate filename in flattened
  ↓
Not duplicated?
  ↓ Yes
Move file with shutil.move()
  ↓
Done
```

## Running the Project

Run `main.py` from the project directory:

```bash
python main.py
```

Make sure the `flattened` directory exists before running the program.

## Current Limitations

This is a beginner-level implementation, so there are still some things that can be improved:

- The path to `flattened` is currently hard-coded.
- Duplicate files are skipped instead of being renamed automatically.
- The `flattened` directory is not explicitly excluded from the scan.
- There is no undo/rollback feature yet.
- There is no command-line interface or user prompt.

## Possible Improvements

Future versions could:

1. Create `flattened` automatically if it does not exist.
2. Exclude `flattened` from `rglob()` scanning.
3. Rename duplicate files automatically, for example `report_1.pdf`.
4. Add an undo feature by storing the original file paths.
5. Let the user choose the source and destination directories.

## Learning Goals

This project is intended to practice:

- `pathlib.Path`
- `Path.rglob()`
- `Path.is_file()`
- `Path.name`
- `shutil.move()`
- Recursive filesystem traversal
- Basic file automation
- Filename collision handling
- Object-oriented Python with `ABC` and `@abstractmethod`
