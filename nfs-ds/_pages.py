from pick import pick
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Symbols:
    OPTION_COVER_LEFT: str = "> "
    OPTION_COVER_RIGHT: str = ""

    @classmethod
    def make_option(cls, name: str) -> str:
        return f"{cls.OPTION_COVER_LEFT}{name}{cls.OPTION_COVER_RIGHT}"

    @classmethod
    def make_options(cls, names: List) -> List:
        return [cls.make_option(name) for name in names]


class PageNavigator:
    DISCONNECT = Symbols.make_option("Disconnect")
    BREAK = ""
    MENU_TITLE = "Navigate through folders or choose an action."

    def __init__(self, stub):
        self._stub = stub
        self._functions = Functions(self._stub)
        self._page_factory = PageFactory()
        self._current_directory = None
        self._dir_tree = None

    def _fetch_dir_tree(self):
        self._dir_tree = self._functions.list_dir("")

    def _get_menu_items(self):
        self._current_directory = None

    def loop_pages(self):
        while True:
            options = self._get_menu_items()
            opt, ind = pick(options, self.MENU_TITLE)

            if opt is self.DISCONNECT:
                break
            elif opt == self.BREAK:
                continue
            elif opt in self._page_factory.pages:
                self._page_factory.create(opt).run(self._current_directory)
            else:
                self._navigate(opt)

