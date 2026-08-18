from pathlib import Path
import shutil
import sys
from abc import ABC, abstractmethod


class BaseFolderDetector(ABC):
    def __init__(self, root):
        self.root = Path(root)
        self.dead_folders = []
    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def analyze(self):
        pass

    @abstractmethod 
    def delete(self):
        pass    

class DeadFolderDetector(BaseFolderDetector):
    
    def scan(self) -> list:
        folders = []
        for file in self.root.rglob("*"):
            if file.is_dir():
                folders.append(file)

        return folders

    def analyze(self, folder: Path) -> bool:
        scanning = list(folder.iterdir())
        return len(scanning) == 1

    def find_dead_folder(self):
        path_folder = self.scan()
        self.dead_folders = [f for f in path_folder if self.analyze(f)]

    @property
    def display(self):
        print(f"There are {len(self.dead_folders)} folders")
        for i in range(len(self.dead_folders)):
            print(f"{i+1} [DEAD] {self.dead_folders[i]}")

    @property
    def delete(self):
        for folders in self.dead_folders:
            shutil.rmtree(folders)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path> [--delete]")
        sys.exit(1)

    delete_mode = "--delete" in sys.argv

    root = sys.argv[1]
    program = DeadFolderDetector(root)
    print(f"Scanning {program.root}")
    print()

    program.find_dead_folder()
    program.display

    if delete_mode and program.dead_folders:
        print()
        answer = input("do you want to delete the folders? (Y/n)")
        if answer.lower() == "y":
            program.delete
            print()
            print("folders deletted succesfully")

        else:
            print("canceled")
            print()
            

if __name__ == "__main__":
    main()