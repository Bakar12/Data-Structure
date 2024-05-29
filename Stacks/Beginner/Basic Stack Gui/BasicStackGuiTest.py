import unittest
from unittest.mock import patch
from tkinter import messagebox

from tqdm import tk

from BasicStackGui import Stack, StackApp

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_to_empty_stack(self):
        self.stack.push('value')
        self.assertEqual(self.stack.display(), ['value'])

    def test_pop_from_empty_stack(self):
        self.assertIsNone(self.stack.pop())

    def test_pop_from_non_empty_stack(self):
        self.stack.push('value')
        self.assertEqual(self.stack.pop(), 'value')

class TestStackApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = StackApp(self.root)
        self.app.stack = Stack()

    @patch.object(messagebox, 'showwarning')
    def test_push_empty_value(self, mock_showwarning):
        self.app.input_value.set('')
        self.app.push_value()
        mock_showwarning.assert_called_once_with("Input Error", "Please enter a value to push.")

    @patch.object(messagebox, 'showwarning')
    def test_pop_from_empty_stack(self, mock_showwarning):
        self.app.pop_value()
        mock_showwarning.assert_called_once_with("Stack Underflow", "The stack is empty. Cannot pop.")

    @patch.object(messagebox, 'showinfo')
    def test_pop_from_non_empty_stack(self, mock_showinfo):
        self.app.stack.push('value')
        self.app.pop_value()
        mock_showinfo.assert_called_once_with("Popped Value", "Popped value: value")

    def test_display_empty_stack(self):
        self.app.display_stack()
        self.assertEqual(self.app.display_area.get("1.0", tk.END).strip(), '')

    def test_display_non_empty_stack(self):
        self.app.stack.push('value')
        self.app.display_stack()
        self.assertEqual(self.app.display_area.get("1.0", tk.END).strip(), 'value')