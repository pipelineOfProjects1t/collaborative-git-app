import unittest

from main import calculate_average_rating, count_books_by_author, is_duplicate


class TestBookTracker(unittest.TestCase):
    def setUp(self):
        self.books = [
            {"author": "Александр Пушкин", "title": "Капитанская дочка", "rating": 5, "read_date": "2026-05-01"},
            {"author": "Фёдор Достоевский", "title": "Игрок", "rating": 4, "read_date": "2026-05-02"},
            {"author": "Александр Пушкин", "title": "Дубровский", "rating": 5, "read_date": "2026-05-03"},
        ]

    def test_average_rating(self):
        self.assertAlmostEqual(calculate_average_rating(self.books), 4.67, places=2)

    def test_average_rating_empty_list(self):
        self.assertEqual(calculate_average_rating([]), 0)

    def test_author_stats(self):
        stats = count_books_by_author(self.books)
        self.assertEqual(stats["Александр Пушкин"], 2)
        self.assertEqual(stats["Фёдор Достоевский"], 1)

    def test_duplicate_book(self):
        self.assertTrue(is_duplicate(self.books, "александр пушкин", "капитанская дочка"))
        self.assertFalse(is_duplicate(self.books, "Николай Гоголь", "Ревизор"))


if __name__ == "__main__":
    unittest.main()
