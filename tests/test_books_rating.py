import csv
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from modules import Books_Rating


class BooksRatingTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        root = Path(self.temp_dir.name)
        self.catalog_file = root / "catalog.csv"
        self.user_file = root / "users.csv"
        self.borrowing_file = root / "borrowings.csv"
        self.ratings_file = root / "ratings.csv"

        self._write_csv(
            self.catalog_file,
            ["ISBN_Number", "Book_Name", "Author"],
            [{"ISBN_Number": "123", "Book_Name": "Test Book", "Author": "A. Writer"}],
        )
        self._write_csv(
            self.user_file,
            ["UserID"],
            [{"UserID": "U001"}, {"UserID": "U002"}],
        )
        self._write_csv(
            self.borrowing_file,
            ["User_ID", "Book_ISBN", "Status"],
            [],
        )

        self.patches = [
            patch.object(Books_Rating, "CATALOG_FILE", self.catalog_file),
            patch.object(Books_Rating, "USER_FILE", self.user_file),
            patch.object(
                Books_Rating, "BORROWING_FILES", (self.borrowing_file,)
            ),
            patch.object(Books_Rating, "RATINGS_FILE", self.ratings_file),
        ]
        for active_patch in self.patches:
            active_patch.start()
            self.addCleanup(active_patch.stop)

    @staticmethod
    def _write_csv(file_path, fieldnames, rows):
        with file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def test_only_borrowers_can_rate_and_existing_rating_is_updated(self):
        success, message = Books_Rating.submit_rating("U001", "123", 5)
        self.assertFalse(success)
        self.assertIn("Only users who have borrowed", message)
        self.assertFalse(self.ratings_file.exists())

        self._write_csv(
            self.borrowing_file,
            ["User_ID", "Book_ISBN", "Status"],
            [{"User_ID": "U001", "Book_ISBN": "123", "Status": "Returned"}],
        )
        success, message = Books_Rating.submit_rating("U001", "123", 5)
        self.assertTrue(success, message)
        success, message = Books_Rating.submit_rating("U001", "123", 3)
        self.assertTrue(success, message)

        self.assertEqual(Books_Rating.get_user_rating("U001", "123"), 3)
        self.assertEqual(Books_Rating.get_rating_summary("123"), (3.0, 1))
        with self.ratings_file.open(newline="", encoding="utf-8") as file:
            self.assertEqual(len(list(csv.DictReader(file))), 1)

    def test_rating_value_must_be_an_integer_between_one_and_five(self):
        for invalid_rating in (0, 6, "not a rating", 2.5, True):
            with self.subTest(rating=invalid_rating):
                success, message = Books_Rating.submit_rating(
                    "U001", "123", invalid_rating
                )
                self.assertFalse(success)
                self.assertIn("between 1 and 5", message)

        self.assertFalse(self.ratings_file.exists())

    def test_new_ratings_update_average_and_count(self):
        self._write_csv(
            self.borrowing_file,
            ["User_ID", "Book_ISBN"],
            [
                {"User_ID": "U001", "Book_ISBN": "123"},
                {"User_ID": "U002", "Book_ISBN": "123"},
            ],
        )
        self.assertTrue(Books_Rating.submit_rating("U001", "123", 2)[0])
        self.assertTrue(Books_Rating.submit_rating("U002", "123", 4)[0])

        self.assertEqual(Books_Rating.get_rating_summary("123"), (3.0, 2))

    def test_book_details_confirms_rating_and_restricts_non_borrowers(self):
        self._write_csv(
            self.borrowing_file,
            ["User_ID", "Book_ISBN"],
            [{"User_ID": "U001", "Book_ISBN": "123"}],
        )
        output = StringIO()
        with patch("builtins.input", side_effect=["Test Book", "5"]):
            with redirect_stdout(output):
                Books_Rating.rate_book({"UserID": "U001"})
        self.assertIn("Your rating has been submitted successfully.", output.getvalue())
        self.assertIn("Average rating: 5.0/5 (1 ratings)", output.getvalue())

        output = StringIO()
        with patch("builtins.input", side_effect=["Test Book", ""]):
            with redirect_stdout(output):
                Books_Rating.rate_book({"UserID": "U001"})
        self.assertIn("Your rating: 5/5 stars", output.getvalue())

        output = StringIO()
        with patch("builtins.input", return_value="123"):
            with redirect_stdout(output):
                Books_Rating.rate_book({"UserID": "U002"})
        self.assertIn(
            "Only users who have borrowed this book can rate it.",
            output.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()
