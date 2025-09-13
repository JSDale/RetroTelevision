import json
import os

class FileLoader:

    def get_file_paths(self):
        root_filepath = self.load_root_filepath()
        sub_folders = [
        f for f in os.listdir(root_filepath)
        if os.path.isdir(os.path.join(root_filepath, f))
        ]

        if not sub_folders:
            sub_folders.append(root_filepath)

        all_videos = []
        for folder in sub_folders:
            all_files = [f for f in os.listdir(folder) 
                         if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith('.mp4')]
            all_videos.append(all_files)

        return all_videos

    def load_root_filepath(self, filepath = None):
        if filepath == None:
            filepath = os.path.join(os.getcwd(), 'appsettings.json')
        with open(filepath, "r") as f:
            config = json.load(f)
        
        return config['RootFilePath']