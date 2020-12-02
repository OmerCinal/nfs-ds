from ._pages import (Copy, Create, Delete, GetFile, Move, Rename, UploadFile,
                     _Page)
from ._symbols import Symbols


class PageFactory:
    def __init__(self):
        self.pages = {
            "Copy": Copy,
            "Move": Move,
            "Rename": Rename,
            "Delete": Delete,
            "Create": Create,
            "Download": GetFile,
            "Upload": UploadFile,
        }

    def create(self, page_name: str, root: str, stub) -> _Page:
        page_name = Symbols.clean(page_name)
        return self.pages[page_name](root=root, stub=stub)
