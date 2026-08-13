from pathlib import Path
from abc import ABC, abstractmethod
import shutil

class Abstract(ABC):
    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def flattened(self):
        pass

class Code(Abstract):
    def scan(self):
        path = Path.cwd()
        for file in path.rglob("*"):
            if file.is_file() and file.name != "main.py":
                self.flattened(path, file)
            

    def flattened(self, path: Path, files: Path):
        flag = True
        flatten_path = Path.cwd() / "flattened"

        for x in flatten_path.rglob(f"*{files.name}"):
            if x.exists():
                flag = False

        if flag:
            shutil.move(str(files), str(path / "flattened"))

def main():
    C = Code()
    C.scan()
if __name__ == "__main__":
    main()