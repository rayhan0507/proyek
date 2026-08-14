from pathlib import Path
import shutil


class FileFlattener:
    def __init__(self, source_path: Path):
        self.source_path = source_path
        self.flattened_path = source_path / "flattened"

    def scan(self):
        self.flattened_path.mkdir(exist_ok=True)

        for file in self.source_path.rglob("*"):
            if not self._is_valid_file(file):
                continue

            self.flatten_file(file)

    def flatten_file(self, file: Path):
        destination = self.flattened_path / file.name

        if destination.exists():
            print(f"Skipped: {file} -> {destination.name} already exists")
            return

        shutil.move(str(file), str(destination))
        print(f"Moved: {file} -> {destination}")

    def _is_valid_file(self, file: Path) -> bool:
        if not file.is_file():
            return False

        if file.name == "main.py":
            return False

        if self.flattened_path in file.parents:
            return False

        return True


def main():
    source_path = Path.cwd()

    flattener = FileFlattener(source_path)
    flattener.scan()


if __name__ == "__main__":
    main()