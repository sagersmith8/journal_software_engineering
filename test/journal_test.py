import journal
import os
import shutil
import unittest


class JournalTest(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.journal_path = os.path.join(os.path.expanduser(os.getcwd()), 'journal')
        cls.journal = journal.Journal(cls.journal_path)

    @classmethod
    def teardown_class(cls):
        shutil.rmtree(cls.journal_path)

    def journal_test(self):
        self.journal.journal_entry("journal")

    def journal_note_test(self):
        self.journal.notes_entry("note")

    def journal_ticket_test(self):
        self.journal.ticket_entry("ticket")

    def journal_todo_test(self):
        self.journal.todo_entry("todo")

    def standup_test(self):
        self.journal.standup(self.journal.journal, None, None)
