from pathlib import Path
import shutil
import sys
from abc import ABC, abstractmethod


class BaseFolderDetector(ABC):
    def __init__(self, root):
        self.root = Path(root)
        self.dead_folder = []
    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def analyze(self):
        pass


class DeadFolderDetector(BaseFolderDetector):
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path> [--delete]")

   
if __name__ == "__main__":
    main()