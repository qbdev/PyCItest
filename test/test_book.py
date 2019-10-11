import unittest
from typing import TypeVar, Generic
from src.book import Book


T = TypeVar('T')


class BasicBookTest(unittest.TestCase, Generic[T]):
    """Test for the Book class"""
    def test_firstBook(self) -> None:
        tester: 'Book' = Book('Monthy', 'Python')
        self.assertEqual(str(tester), 'Monthy by Python')


if __name__ == '__main__':
    unittest.main()
