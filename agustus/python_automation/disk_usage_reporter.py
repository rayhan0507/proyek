from pathlib import Path
from abc import ABC, abstractmethod

class Entitas_disk:
    @abstractmethod
    def analyzer(self):
        pass

class Disk(Entitas_disk):
    def __init__(self, disk):
        self.disk = disk
    def analyzer(self):
        total_ukuran_path = 0
        total_jumlah_file = 0
        total_folder = 0

        path = Path(self.disk)

        ekstensi = {}

        for file in path.iterdir():
            if file.is_file():
                total_jumlah_file += 1
                ekstensi[file.suffix] = ekstensi.get(file.suffix, 0) + 1

            elif file.is_dir():
                total_folder += 1

            size = file.stat().st_size
            total_ukuran_path += size
            total_jumlah_file += 1



        print(f"total ukuran path: {total_ukuran_path // 1000} MB")
        print(f"total file: {total_jumlah_file}")
        print(f"total folder: {total_folder}")
        print("\n")
        print("=====total ekstensi=====")
        for key, val in ekstensi.items():
            print(f"{key}: {val} KB")

def main():
    input_Path = input("masukan path tanpa driver letter (C:. D:, E:): ")
    D = Disk(input_Path)
    D.analyzer()

if __name__ == "__main__":
    main()