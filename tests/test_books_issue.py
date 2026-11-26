import csv
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date, timedelta
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from modules import Books_Issue


class BooksIssueTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        root = Path(self.temp_dir.name)
        self.user_file = root / "users.csv"
        self.catalog_file = root / "catalog.csv"
        self.borrowing_file = root / "borrowings.csv"
        self.legacy_borrowing_file = root / "legacy_borrowings.csv"

        self._write_csv(
            self.user_file,
            ["UserID"],
            [{"UserID": "U001"}, {"UserID": "U002"}],
        )
        self._write_csv(
            self.catalog_file,
            ["ISBN_Number", "Book_Name", "Author"],
            [
                {"ISBN_Number": "123", "Book_Name": "Test Book", "Author": "A. Writer"},
                {"ISBN_Number": "456", "Book_Name": "Other Book", "Author": "B. Writer"},
            ],
        )
        self._write_csv(
            self.borrowing_file,
            Books_Issue.BORROWING_FIELDS,
            [],
        )
        self._write_csv(
            self.legacy_borrowing_file,
            Books_Issue.BORROWING_FIELDS,
            [],
        )

        active_patches = (
            patch.object(Books_Issue, "USER_FILE", self.user_file),
            patch.object(Books_Issue, "CATALOG_FILE", self.catalog_file),
            patch.object(Books_Issue, "BORROWING_FILE", self.borrowing_file),
            patch.object(
                Books_Issue,
                "LEGACY_BORROWING_FILE",
                self.legacy_borrowing_file,
            ),
        )
        for active_patch in active_patches:
            active_patch.start()
            self.addCleanup(active_patch.stop)

    @staticmethod
    def _write_csv(file_path, fieldnames, rows):
        with file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def test_issue_creates_seven_day_record_and_confirms(self):
        issue_date = date(2026, 11, 25)
        success, message, record = Books_Issue.issue_book_record(
            "U001", "123", issue_date
        )

        self.assertTrue(success)
        self.assertEqual(message, "Book issued successfully")
        self.assertEqual(record["Issue_Date"], "2026-11-25")
        self.assertEqual(record["Expiry_Date"], "2026-12-02")
        self.assertTrue(Books_Issue.has_book_access("U001", "123", issue_date))

        with self.borrowing_file.open(newline="", encoding="utf-8") as file:
            self.assertEqual(list(csv.DictReader(file)), [record])

    def test_rejects_unregistered_user_and_missing_book(self):
        result = Books_Issue.issue_book_record("U999", "123")
        self.assertEqual(result, (False, "User not found", None))

        result = Books_Issue.issue_book_record("U001", "999")
        self.assertEqual(result, (False, "E-book not found", None))

        with self.borrowing_file.open(newline="", encoding="utf-8") as file:
            self.assertEqual(list(csv.DictReader(file)), [])

    def test_only_one_active_issue_per_book(self):
        issue_date = date(2026, 11, 25)
        self.assertTrue(
            Books_Issue.issue_book_record("U001", "123", issue_date)[0]
        )
        self.assertEqual(
            Books_Issue.issue_book_record("U002", "123", issue_date),
            (False, "Book currently unavailable", None),
        )

    def test_expired_book_becomes_available_and_is_marked_returned(self):
        issue_date = date(2026, 11, 25)
        expiry_date = issue_date + timedelta(days=7)
        self.assertTrue(
            Books_Issue.issue_book_record("U001", "123", issue_date)[0]
        )

        success, _, record = Books_Issue.issue_book_record(
            "U002", "123", expiry_date
        )
        self.assertTrue(success)
        with self.borrowing_file.open(newline="", encoding="utf-8") as file:
            records = list(csv.DictReader(file))
        self.assertEqual(records[0]["Status"], "Returned")
        self.assertEqual(records[0]["Return_Date"], expiry_date.isoformat())
        self.assertEqual(record["User_ID"], "U002")

    def test_issue_menu_search_and_success_message(self):
        output = StringIO()
        with patch("builtins.input", return_value="Test Book"):
            with redirect_stdout(output):
                Books_Issue.issue_book({"UserID": "U001"})

        self.assertIn("Book issued successfully", output.getvalue())
        self.assertIn("Issue date:", output.getvalue())
        self.assertIn("Due date:", output.getvalue())

    def test_rejects_unknown_title_in_interactive_flow(self):
        output = StringIO()
        with patch("builtins.input", return_value="No such title"):
            with redirect_stdout(output):
                Books_Issue.issue_book({"UserID": "U001"})
        self.assertIn("E-book not found", output.getvalue())


if __name__ == "__main__":
    unittest.main()
