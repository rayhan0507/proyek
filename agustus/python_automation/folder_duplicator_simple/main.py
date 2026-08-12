from pathlib import Path
import shutil
from abc import ABC, abstractmethod

class Abstraksi(ABC):
    @abstractmethod
    def analyze(self):
        pass
    
class Code(Abstraksi):
    def analyze(self):
        path = Path.cwd()
        source_path = path / "source"
        shutil.copytree(source_path, "backup")
        
def main():
    C = Code()
    C.analyze()

if __name__ == "__main__":
    main()