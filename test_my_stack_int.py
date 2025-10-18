import unittest
from main import MyStackInt

class TestMyStackInt(unittest.TestCase):

    def test_push_and_pop(self):
        stack = MyStackInt()
        stack.push(5)
        stack.push(10)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.pop(), 5)

    def test_max_single_element(self):
        stack = MyStackInt()
        stack.push(42)
        self.assertEqual(stack.max(), 42)

    def test_max_multiple_elements(self):
        stack = MyStackInt()
        stack.push(5)
        stack.push(10)
        stack.push(3)
        self.assertEqual(stack.max(), 10)

    def test_max_after_pop(self):
        stack = MyStackInt()
        stack.push(5)
        stack.push(10)
        stack.push(3)
        stack.pop()
        self.assertEqual(stack.max(), 10)
        stack.pop()
        self.assertEqual(stack.max(), 5)

    def test_pop_empty_stack(self):
        stack = MyStackInt()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_max_empty_stack(self):
        stack = MyStackInt()
        with self.assertRaises(IndexError):
            stack.max()

    def test_max_with_negative_numbers(self):
        stack = MyStackInt()
        stack.push(-5)
        stack.push(-10)
        stack.push(-3)
        self.assertEqual(stack.max(), -3)

if __name__ == '__main__':
    unittest.main()