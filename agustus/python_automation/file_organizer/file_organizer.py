from pathlib import Path
from abc import ABC, abstractmethod
import shutil

class Entitas(ABC):
    @abstractmethod
    def organize(self):
        pass

class File(Entitas):
    def __init__(self, path):
        self.path = path

    def organize(self):
        path = Path(self.path)
        ekstensi = {}

        for file in path.iterdir():
            ekstensi[file.suffix] = ekstensi.get(file.suffix, 1)

        for x, _ in ekstensi.items():
            nama_folder = x.lstrip(".")
            new_folder = path / nama_folder
            new_folder.mkdir(parents=True, exist_ok=True)

        for file in path.iterdir():
            if file.is_file():
                nama_folder = file.suffix.lstrip(".") if file.suffix else "tanpa ekstensi"
                new_folder = path / nama_folder
                shutil.move(str(file), str(new_folder / file.name))




def main():
    input_path = input("masukan path yang ingin di rapihkan tanpa driver letter (C: D: E:): ")
    C = File(input_path)
    C.organize()
    
if __name__ == "__main__":
    main()
