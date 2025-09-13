import json
import os

class FileLoader:

    def get_file_paths(self):
        root_filepath = self.load_root_filepath()
        print(root_filepath)

    def load_root_filepath(self, filepath = None):
        if filepath == None:
            filepath = os.path.join(os.getcwd(), 'appsettings.json')
        with open(filepath, "r") as f:
            config = json.load(f)
        
        return config['RootFilePath']