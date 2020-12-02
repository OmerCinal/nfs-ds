from pick import pick
from typing import List, Dict
from ._explorer import Explorer
from ._symbols import Symbols
from ._functions import Functions
from ._page_factory import PageFactory


class PageNavigator:
    DISCONNECT = Symbols.make_option("Disconnect")
    BREAK = " "
    MENU_TITLE = "Navigate through folders or choose an action."

    def __init__(self, stub):
        self._stub = stub
        self._functions = Functions(self._stub)
        self._page_factory = PageFactory()
        
        self._explorer = Explorer("", self._stub)

    def _get_actions(self) -> List:
        actions = sorted(Symbols.make_options(self._page_factory.pages.keys()))
        return actions + [self.BREAK, self.DISCONNECT]

    def _get_menu_items(self) -> List:
        return (
            self._explorer.ls()
            + [self.BREAK]
            + self._get_actions()
        )

    def loop_pages(self):
        while True:
            options = self._get_menu_items()
            opt, ind = pick(options, self.MENU_TITLE)

            if opt is self.DISCONNECT:
                break
            elif opt == self.BREAK:
                continue
            elif Symbols.clean(opt) in self._page_factory.pages:
                self._page_factory.create(opt, root=self._explorer.root, stub=self._stub).run()
            elif opt in self._explorer.get_folders():
                self._explorer.cd(opt)
            elif opt in self._explorer.get_files():
                self._functions.get_file_info(self._explorer.get_path(opt))
            else:
                raise Exception(f"Selected {opt} is unrecognized.")
