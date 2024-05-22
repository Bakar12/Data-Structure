import unittest
from unittest.mock import patch
from io import StringIO
from Array.Beginner.ArrayDouble.ArrayDoubling import DoubleArray


class TestDoubleArray(unittest.TestCase):

    # Set up method to create a new DoubleArray instance before each test
    def setUp(self):
        self.array = DoubleArray()

    # Test that a new DoubleArray instance is initialized correctly
    def test_initialization(self):
        self.assertEqual(len(self.array), 0)
        self.assertEqual(self.array.capacity, 1)

    # Test that appending an item and getting an item work correctly
    def test_append_and_get_item(self):
        self.array.append("test")
        self.assertEqual(self.array[0], "test")
        self.assertEqual(len(self.array), 1)

    # Test that setting an item at a specific index works correctly
    def test_set_item(self):
        self.array.append("test")
        self.array[0] = "new"
        self.assertEqual(self.array[0], "new")

    # Test that the array is resized correctly when it's full
    def test_resize(self):
        for i in range(10):
            self.array.append(i)
        self.assertEqual(len(self.array), 10)
        self.assertEqual(self.array.capacity, 16)

    # Test that an IndexError is raised when trying to set an item at an out-of-range index
    def test_index_error(self):
        with self.assertRaises(IndexError):
            self.array[0] = "test"

    # Test that the input_until_quit method works correctly
    @patch('builtins.input', side_effect=['test1', 'test2', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_input_until_quit(self, mock_stdout):
        self.array.input_until_quit()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output, ['Capacity: 1, Length: 1', 'Capacity: 2, Length: 2'])


if __name__ == '__main__':
    unittest.main()
