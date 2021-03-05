import unittest
import os
import io
import sys

from src.records_handler import RecordsHandler

# Boundary from Right-BICEP is considered in the test cases
# Inverse relationship from Right-BICEP is considered in the test cases
# Cross-check form Right-BICEP is considered in the test cases
# Error conditions from Right-BICEP is considered in the test cases by using assertions

class TestRecordsHandler(unittest.TestCase):
    def setUp(self):
        # Not mocking any object because it is time consuming to
        # discover mocking for this Lab.
        self.recordsHandler = RecordsHandler("resources/lab3DB.db")
        # Making sure that there are no records in each test case
        self.recordsHandler.delete_all()

    def test_add_record(self):
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        self.recordsHandler.list_all()
        # No records found
        self.assertEqual(capturedOutput.getvalue(), "")

        self.recordsHandler.add_record("name", "email", "age", "origin")
        self.recordsHandler.list_all()  # Call unchanged function.
        sys.stdout = sys.__stdout__  # Reset redirect.

        # Added record found
        self.assertEqual(
            capturedOutput.getvalue(), "(1, 'name', 'email', 'age', 'origin')\n"
        )

    def test_list_all(self):
        self.recordsHandler.add_record("name", "email", "age", "origin")

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.recordsHandler.list_all()  # Call unchanged function.
        sys.stdout = sys.__stdout__  # Reset redirect.

        self.assertEqual(
            capturedOutput.getvalue(), "(1, 'name', 'email', 'age', 'origin')\n"
        )

    def test_look(self):
        record = self.recordsHandler.look("email2", "age2")
        self.assertEqual(record, [])

        self.recordsHandler.add_record("name2", "email2", "age2", "origin2")
        record = self.recordsHandler.look("email2", "age2")
        self.assertEqual(record[0], (1, "name2", "email2", "age2", "origin2"))

    def test_delete_record(self):
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.

        self.recordsHandler.list_all()
        self.assertEqual(capturedOutput.getvalue(), "")

        self.recordsHandler.add_record("name1", "email1", "age1", "origin1")
        self.recordsHandler.add_record("name2", "email2", "age2", "origin2")
        self.recordsHandler.add_record("name3", "email3", "age3", "origin3")

        self.recordsHandler.list_all()

        self.assertEqual(
            capturedOutput.getvalue(),
            "(1, 'name1', 'email1', 'age1', 'origin1')\n"
            "(2, 'name2', 'email2', 'age2', 'origin2')\n"
            "(3, 'name3', 'email3', 'age3', 'origin3')\n",
        )

        self.recordsHandler.delete_record(1)

        capturedOutput = io.StringIO("")  # Clearing buffer
        sys.stdout = capturedOutput

        self.recordsHandler.list_all()

        self.assertEqual(
            capturedOutput.getvalue(),
            "(2, 'name2', 'email2', 'age2', 'origin2')\n"
            "(3, 'name3', 'email3', 'age3', 'origin3')\n",
        )

        sys.stdout = sys.__stdout__  # Reset redirect.

    def tearDown(self):
        self.recordsHandler.close_connection()
