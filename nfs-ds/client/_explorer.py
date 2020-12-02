from typing import Dict, List
import os


class Explorer:
    FOLDERS = "folders"
    FILES = "files"
    PARENT = ".."

    def __init__(self, tree: Dict, pwd: str = None):
        self.tree = tree
        self.pwd = pwd or min(tree.keys(), key=lambda x: x.count(os.sep))

    def cd(self, folder: str):
        folder = os.path.normpath(folder)
        # cd ..
        if folder == self.PARENT:
            self.pwd = os.path.basename(self.pwd)
        # cd folder
        elif folder in self.tree[self.pwd][self.FOLDERS]:
            self.pwd = os.path.join(self.pwd, folder)
        # something aint right
        else:
            raise Exception(f"{folder} doesn't exist in {self.pwd}")

    def get_folders(self) -> List:
        return [self.PARENT] + sorted(self.tree[self.pwd][self.FOLDERS])

    def get_files(self) -> List:
        return sorted(self.tree[self.pwd][self.FILES])
