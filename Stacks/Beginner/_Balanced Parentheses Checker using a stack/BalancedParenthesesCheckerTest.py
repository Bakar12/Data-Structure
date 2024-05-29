import unittest
from unittest.mock import patch
from tkinter import messagebox

from tqdm import tk

from BalancedParenthesesChecker import ParenthesesChecker

class ParenthesesCheckerTests(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.checker = ParenthesesChecker(self.root)

    def check_balance_on_balanced_input(self):
        self.checker.input_string.set('()')
        self.checker.check_balance()
        self.assertEqual(self.checker.result_label.cget("text"), "The parentheses are balanced.")

    def check_balance_on_unbalanced_input(self):
        self.checker.input_string.set('((')
        self.checker.check_balance()
        self.assertEqual(self.checker.result_label.cget("text"), "The parentheses are not balanced.")

    def is_balanced_on_balanced_input(self):
        self.assertTrue(self.checker.is_balanced('()'))

    def is_balanced_on_unbalanced_input(self):
        self.assertFalse(self.checker.is_balanced('(('))

    def is_balanced_on_empty_input(self):
        self.assertTrue(self.checker.is_balanced(''))

    @patch.object(messagebox, 'showinfo')
    def check_balance_on_empty_input(self, mock_showinfo):
        self.checker.input_string.set('')
        self.checker.check_balance()
        mock_showinfo.assert_called_once_with("Input Error", "Please enter a string to check.")