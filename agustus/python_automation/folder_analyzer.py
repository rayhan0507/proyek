from abc import ABC, abstractmethod
from pathlib import Path

class EntitasFolder(ABC):
    @abstractmethod
    def analyzer(self):
        pass

class Folder(EntitasFolder):
    def __init__(self, path):
        self.path = path

    def analyzer(self):
        path = Path(self.path)
        jumlah_file = 0
        Jumlah_folder = 0

        dictionary = {}

        cari = path.rglob("*")
        for x in cari:
            if x.is_file():
                jumlah_file += 1
                dictionary[x.suffix] = dictionary.get(x.suffix, 0) + 1

            elif x.is_dir():
                Jumlah_folder += 1


        print(f"jumlah file :{jumlah_file}")
        print(f"jumlah folder : {Jumlah_folder}")
        print("jumlah suffix file")
        for key, val in dictionary.items():
            label = key if key else "non ekstensi"
            print(f"{label}: {val}")

def main():
    input_path = input("input path anda tanpa driver letter (C:, D: E:): ")
    F = Folder(input_path)
    F.analyzer()


if __name__ == "__main__":
    main()