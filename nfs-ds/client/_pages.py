from ._explorer import Explorer
from ._symbols import Symbols
from ._functions import Functions
from abc import ABC, abstractmethod
from pick import pick
import os


# Page interface
class _Page(ABC):
    @abstractmethod
    def run(self):
        pass

# Page baseclass
class _Navigatable:
    BREAK = " "
    HERE = Symbols.make_option("Select this folder")
    CANCEL = Symbols.make_option("Cancel")
    FOLDER_TYPE = "folder_type"
    FILE_TYPE = "file_type"

    def __init__(self, root: str, stub):
        self._explorer = Explorer(root, stub)
        self._functions = Functions(stub)

    def _confirm(self, question: str) -> str:
        option, index = pick(Symbols.make_options(["No", "Yes"]), question)
        return option == "Yes"


# Pages # 
class Copy(_Page, _Navigatable):
    def _copy(self, source: str, sink: str, copy_type: str):
        if self._confirm(f"Are you sure you want to copy {source} to {sink}?"):
            if copy_type == self.FOLDER_TYPE:
                self._functions.copy_dir(source=source, sink=sink)
            else:
                self._functions.copy_file(source=source, sink=sink)
    
    def _get_source(self, title: str):
        copy_type = None
        source = None
        while True:
            options = self._explorer.ls() + [self.BREAK, self.CANCEL]
            opt, ind = pick(options, title)

            if opt == self.BREAK:
                continue
            elif opt == self.CANCEL:
                break
            elif opt in self._explorer.get_folders():
                copy_type = self.FOLDER_TYPE
                source = self._explorer.get_path(opt)
                break
            elif opt in self._explorer.get_files():
                copy_type = self.FILE_TYPE
                source = self._explorer.get_path(opt)
                break

        return source, copy_type

    def _get_sink_folder(self, title: str):
        sink = None
        while  True:
            options = self._explorer.ls() + [self.BREAK, self.HERE, self.CANCEL]
            opt, ind = pick(options, title)

            if opt == self.BREAK or opt in self._explorer.get_files():
                continue
            elif opt == self.CANCEL:
                break
            elif opt == self.HERE:
                sink = self._explorer.root
                break
            elif opt in self._explorer.get_folders():
                self._explorer.cd(opt)

        return sink

    def run(self):
        source, copy_type = self._get_source("Select the source file or folder to copy")
        sink = None
        if source is not None:
            sink = self._get_sink_folder("Select the destination folder to copy")
            sink = os.path.join(sink, os.path.basename(source))

        if source is not None and sink is not None:
            if copy_type == self.FOLDER_TYPE:
                self._functions.copy_dir(source=source, sink=sink)
            else:
                self._functions.copy_file(source=source, sink=sink)




class Move(_Page, _Navigatable):
    def run(self):
        pass


class Rename(_Page, _Navigatable):
    def run(self):
        pass


class Delete(_Page, _Navigatable):
    def run(self):
        pass


class Create(_Page, _Navigatable):
    def run(self):
        pass


class GetFile(_Page, _Navigatable):
    def run(self):
        pass


class UploadFile(_Page, _Navigatable):
    def run(self):
        pass


