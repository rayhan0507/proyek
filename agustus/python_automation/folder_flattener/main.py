from abc import ABC, abstractmethod
from pathlib import Path
import shutil


class FileProcessor(ABC):

    @abstractmethod
    def scan(self) -> None:
        """Scan files from the source directory."""
        pass

    @abstractmethod
    def process_file(self, file: Path) -> None:
        """Process a single file."""
        pass


class FileFlattener(FileProcessor):

    def __init__(self, source_path: Path):
        self.source_path = source_path
        self.flattened_path = source_path / "flattened"

    def scan(self) -> None:
        self.flattened_path.mkdir(exist_ok=True)

        for file in self.source_path.rglob("*"):
            if not self._is_valid_file(file):
                continue

            self.process_file(file)

    def process_file(self, file: Path) -> None:
        destination = self.flattened_path / file.name

        if destination.exists():
            print(
                f"Skipped: {file} "
                f"-> {destination.name} already exists"
            )
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


def main() -> None:
    source_path = Path.cwd()

    flattener = FileFlattener(source_path)
    flattener.scan()


if __name__ == "__main__":
    main()