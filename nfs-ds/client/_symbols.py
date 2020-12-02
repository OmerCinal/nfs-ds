from dataclasses import dataclass
from typing import List

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

    @classmethod
    def clean(cls, name: str) -> str:
        return name.strip(cls.OPTION_COVER_LEFT).strip(cls.OPTION_COVER_RIGHT)
