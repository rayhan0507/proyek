from pathlib import Path
from abc import ABC, abstractmethod
import shutil
import argparse

class Base_suspicious_file_scanner(ABC):
    def __init__(self, root: Path):
        self.root = Path(root)
        self.DANGEROUS_WORDS = ["crack", "keygen", "payload", "exploit", "trojan", "backdoor"]
        self.EXTENSION_EXECUTABLE = [".exe", ".scr", ".bat", ".cmd", ".js", ".vbs", ".msi"]
        self.DOCUMENT_EXTENSIONS = [".pdf", ".doc", "docx", ".xls", "xlsx", ",jpg", ".jpeg", ".png", ".txt"]
        self.SMALL_LIMIT_EXE_BYTE = 10 * 1024
        
        self.suspicious_extensions = []
        self.suspicious_filenames = []


    
class Suspicious_file_scanner(Base_suspicious_file_scanner):

    def analyze_suffix(self):
        for file in self.root.rglob("*"):
            if file.suffix in self.EXTENSION_EXECUTABLE:
                self.suspicious_extensions.append(file)

    def find_suspicious_file(self):
        suffix = self.analyze_suffix()
        print(suffix)


def main():
    parser = argparse.ArgumentParser()
    parser.usage = "Run like this: file.py [-v]" 
    parser.add_argument("-v", "--verbose", help="provides a verbose description")

    args: argparse.Namespace = parser.parse_args()

    root = args.verbose
    program = Suspicious_file_scanner(root)
    program.find_suspicious_file()


if __name__ == "__main__":
    main()