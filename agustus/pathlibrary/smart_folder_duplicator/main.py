from pathlib import Path
import shutil
from abc import ABC, abstractmethod  

class Abstract(ABC):
    @abstractmethod
    def folder_unik(self):
        pass
    @abstractmethod
    def cek_folder(self):
        pass
    
class Code(Abstract):
    def __init__(self, jumlah_copy: Path, path_folder: Path):
        self.jumlah_copy = jumlah_copy
        self.path_folder = path_folder

    def folder_unik(self, destinasi, copy_file):
        i = 1
        while i <= copy_file:
            shutil.copytree(str(destinasi), str(destinasi.parent / f"Sample_project_{i}"))
            i+=1

    def cek_folder(self):
        if not self.path_folder.exists():
            raise FileNotFoundError("folder tidak di temukan")
        if self.path_folder.exists():
            self.folder_unik(self.path_folder, self.jumlah_copy)

if __name__ == "__main__":
        destinasi_path = input("masukan path folder: ")
        copy = int(input("berapa copy: "))
        path = Path(destinasi_path[2:])
        C = Code(copy, path)
        C.cek_folder()