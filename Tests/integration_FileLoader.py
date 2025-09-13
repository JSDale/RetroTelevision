import sys
import os

# Add src/ folder to sys.path so RetroTelevision is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from RetroTelevision import FileLoader

def run():
    loader = FileLoader()
    files = loader.get_file_paths()
    index = 0
    for file in files:
        print(f'index: {index}')
        for f in file:
            print(f)
        index = index + 1

if __name__ == "__main__":
    run()