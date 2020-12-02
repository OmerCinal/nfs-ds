from _pages import (
    CopyDir,
    DeleteDir,
    GetFile,
    UploadFile,
    CreateDir,
    RenameDir,
    MoveDir,
    DeleteFile,
    RenameFile,
    CopyFile,
    MoveFile,
)

class PageFactory:
    def __init__(self):
        self.pages = {
            "copy_dir": CopyDir,
            "delete_dir": DeleteDir,
            "get_file": GetFile,
            "upload_file": UploadFile,
            "create_dir": CreateDir,
            "rename_dir": RenameDir,
            "move_dir": MoveDir,
            "delete_file": DeleteFile,
            "rename_file": RenameFile,
            "copy_file": CopyFile,
            "move_file": MoveFile,
        } 
    def create(self, page_name: str, tree: str, pwd: str):
        return self.pages[page_name](tree=tree, pwd=pwd)
