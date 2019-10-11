from typing import TypeVar, Generic


T = TypeVar('T')


class Book(Generic[T]):
    """Class for the Book object"""
    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author

    def __repr__(self) -> str:
        return "{} by {}".format(self.title, self.author)
