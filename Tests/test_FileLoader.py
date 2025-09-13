from RetroTelevision import FileLoader
import pytest

def test_can_load_root_filepath():
    loader = FileLoader()
    path = loader.load_root_filepath()
    print(path)
    assert path is not None
