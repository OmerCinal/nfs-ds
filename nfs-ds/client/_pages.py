from _explorer import Explorer
from abc import ABC, abstractmethod
from pick import pick
import os


class _Page(ABC):
    @abstractmethod
    def run(self):
        pass


class _Navigatable:
    def __init__(self, tree: str, pwd: str):
        self._tree = tree
        self._explorer = Explorer(self._tree, pwd)


class CopyDir(_Page, _Navigatable):
    def run(self):
        pass


class DeleteDir(_Page, _Navigatable):
    def run(self):
        pass


class GetFile(_Page, _Navigatable):
    def run(self):
        pass


class UploadFile(_Page, _Navigatable):
    def run(self):
        pass


class CreateDir(_Page, _Navigatable):
    def run(self):
        pass


class RenameDir(_Page, _Navigatable):
    def run(self):
        pass


class MoveDir(_Page, _Navigatable):
    def run(self):
        pass


class DeleteFile(_Page, _Navigatable):
    def run(self):
        pass


class RenameFile(_Page, _Navigatable):
    def run(self):
        pass


class CopyFile(_Page, _Navigatable):
    def run(self):
        pass


class MoveFile(_Page, _Navigatable):
    def run(self):
        pass

