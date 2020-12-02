from ._explorer import Explorer
from ._symbols import Symbols
from ._functions import Functions
from abc import ABC, abstractmethod
from pick import pick
import os


# Page interface
class _Page(ABC):
    @abstractmethod
    def run(self) -> bool:
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

    def _confirm(self, question: str) -> bool:
        option, index = pick(Symbols.make_options(["No", "Yes"]), question)
        return Symbols.clean(option) == "Yes"

    def _get_source(self, title: str):
        source_type = None
        source = None
        while True:
            options = self._explorer.ls() + [self.BREAK, self.CANCEL]
            opt, ind = pick(options, title)

            if opt == self.BREAK:
                continue
            elif opt == self.CANCEL:
                break
            elif opt in self._explorer.get_folders():
                source_type = self.FOLDER_TYPE
                source = self._explorer.get_path(opt)
                break
            elif opt in self._explorer.get_files():
                source_type = self.FILE_TYPE
                source = self._explorer.get_path(opt)
                break

        return source, source_type

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

    def _get_sink_file(self, title: str):
        sink = None
        while  True:
            options = self._explorer.ls() + [self.BREAK, self.CANCEL]
            opt, ind = pick(options, title)

            if opt == self.BREAK:
                continue
            elif opt == self.CANCEL:
                break
            elif opt in self._explorer.get_files():
                sink = os.path.join(self._explorer.root, opt)
                break
            elif opt in self._explorer.get_folders():
                self._explorer.cd(opt)

        return sink

    def _get_text_input(self, title: str) -> str:
        return input(f"{title}\n>>") or None


# Pages # 
class Copy(_Page, _Navigatable):
    def run(self) -> bool:
        source, source_type = self._get_source("Select the source file or folder to copy")
        sink = None
        successful = False
        if source is not None:
            sink = self._get_sink_folder("Select the destination folder to copy")
            if sink is not None:
                if source_type == self.FOLDER_TYPE:
                    func = self._functions.copy_dir
                else:
                    sink = os.path.join(sink, os.path.basename(source))
                    func = self._functions.copy_file

                question = (
                    "Are you sure you want to proceed?\n"
                    + f"Source: {source}\n"
                    + f"Destination: {sink}"
                )
                if self._confirm(question):
                    func(source=source, sink=sink)
                    successful = True

        return successful


class Move(_Page, _Navigatable):
    def run(self) -> bool:
        source, source_type = self._get_source("Select the source file or folder to move")
        sink = None
        successful = False
        if source is not None:
            sink = self._get_sink_folder("Select the destination folder to move")
            if sink is not None:
                if source_type == self.FOLDER_TYPE:
                    func = self._functions.move_dir
                else:
                    sink = os.path.join(sink, os.path.basename(source))
                    func = self._functions.move_file

                question = (
                    "Are you sure you want to proceed?\n"
                    + f"Source: {source}\n"
                    + f"Destination: {sink}"
                )
                if self._confirm(question):
                    func(source=source, sink=sink)
                    successful = True

        return successful


class Rename(_Page, _Navigatable):
    def run(self) -> bool:
        source, source_type = self._get_source("Select a file or a folder to rename")
        successful = False
        if source is not None:
            new_name = self._get_text_input(f"Rename {os.path.basename(source)} to?")
            new_name = os.path.join(os.path.dirname(source), new_name)
            if new_name is not None:
                if source_type == self.FOLDER_TYPE:
                    func = self._functions.rename_dir
                else:
                    func = self._functions.rename_file

                question = (
                    "Are you sure you want to rename the file?\n"
                    + f"Original: {os.path.basename(source)}\n"
                    + f"New name: {os.path.basename(new_name)}"
                )

                if self._confirm(question):
                    successful = func(source=source, sink=new_name)

        return successful


class Delete(_Page, _Navigatable):
    def run(self) -> bool:
        source, source_type = self._get_source("Select a file or a folder to remove")
        successful = False
        if source is not None:    
            if source_type == self.FOLDER_TYPE:
                func = self._functions.delete_dir
            else:
                func = self._functions.delete_file

            question = (
                "Are you sure you want to remove the file/folder?\n"
                + f"{os.path.basename(source)}\n"
            )

            if self._confirm(question):
                successful = func(source)

        return successful


class Create(_Page, _Navigatable):
    def run(self) -> bool:
        folder_name = self._get_text_input("Enter a folder name.")
        successful = False
        if folder_name is not None and self._confirm(f"Do you want to create {folder_name} in \n{self._explorer.root}"):
            successful = self._functions.create_dir(os.path.join(self._explorer.root, folder_name))

        return successful


class GetFile(_Page, _Navigatable):
    def run(self) -> bool:
        pass


class UploadFile(_Page, _Navigatable):
    def run(self) -> bool:
        pass


