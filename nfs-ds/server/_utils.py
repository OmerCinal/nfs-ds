import os
import shutil
from typing import Any


def copy_tree(src: str, dst: str, symlinks: bool = False, ignore: Any = None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
