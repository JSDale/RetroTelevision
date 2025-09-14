import json
import os

class FileLoader:

    def get_file_paths(self):
        root_filepath = self._load_root_filepath()
        sub_folders = [
        f for f in os.listdir(root_filepath)
        if os.path.isdir(os.path.join(root_filepath, f))
        ]

        if not sub_folders:
            sub_folders.append(root_filepath)

        all_videos = []
        for folder in sub_folders:
            all_files = []
            for file_name in os.listdir(folder):
                full_path = os.path.join(folder, file_name)
                if os.path.isfile(full_path) and (file_name.lower().endswith('.mp4') or file_name.lower().endswith('.mkv')):
                    all_files.append(full_path)
            all_videos.append(all_files)

        return all_videos

    def _load_root_filepath(self, filepath = None):
        if filepath == None:
            filepath = os.path.join(os.getcwd(), 'appsettings.json')
        with open(filepath, "r") as f:
            config = json.load(f)
        
        return config['RootFilePath']