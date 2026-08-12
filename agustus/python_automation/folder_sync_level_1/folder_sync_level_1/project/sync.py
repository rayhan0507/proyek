from pathlib import Path
import shutil
from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def analyze(self):
        pass

class Code(Abstract):
    def analyze(self):
        path_source = Path(r"C:\Users\rayhan\Downloads\folder_sync_level_1\folder_sync_level_1\source")
        path_target = Path(r"C:\Users\rayhan\Downloads\folder_sync_level_1\folder_sync_level_1\target")

        dict_file = {}

        for file in path_source.iterdir():
            dict_file[file.name] = dict_file.get(file.name, 0) + 1      

        for file in path_target.iterdir():
            dict_file[file.name] = dict_file.get(file.name, 0) + 1

        for x, _ in dict_file.items():
            if dict_file[x] == 1:
                folder = path_source / x
                shutil.move(str(folder), str(path_target / x))
def main():
    C = Code()
    C.analyze()
if __name__ == "__main__":
    main()