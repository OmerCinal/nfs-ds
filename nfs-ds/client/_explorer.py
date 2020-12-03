import os
from typing import Dict, List

from ._functions import Functions


class _Explorer:
    PARENT = ".."

    def cd(self, folder: str):
        folder = os.path.normpath(folder)
        # cd ..
        if folder == self.PARENT:
            path = os.path.dirname(self.root)
        # cd folder
        elif folder in self.folders:
            path = os.path.join(self.root, folder)
        # something aint right
        else:
            raise Exception(f"{folder} doesn't exist in {self.root}")

        self.update_tree(path)

    def get_folders(self) -> List:
        return [self.PARENT] + sorted(self.folders)

    def get_files(self) -> List:
        return sorted(self.files)

    def ls(self):
        return self.get_folders() + self.get_files()

    def get_path(self, file: str) -> str:
        return os.path.join(self.root, file)


class RemoteExplorer(_Explorer):
    def __init__(self, root: Dict, stub):
        self._functions = Functions(stub)
        self.update_tree(root)

    def update_tree(self, root: str):
        tree = self._functions.list_dir(root)
        if tree is not None:
            self.root = tree["root"]
            self.folders = tree["folders"]
            self.files = tree["files"]


class LocalExplorer(_Explorer):
    def __init__(self):
        self.update_tree(os.path.expanduser("~"))

    def update_tree(self, root: str):
        self.root, self.folders, self.files = next(os.walk(root))
