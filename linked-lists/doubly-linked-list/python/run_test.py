from LinkedList import Linked_list
from Node import Node

from collections.abc import Iterator

import unittest



class TestList(unittest.TestCase):
    list = Linked_list()

    # Runs before eveery test
    def setUp(self):
        self.list = Linked_list()

    def test_iterator_init(self):
        self.list = iter(self.list)
        self.assertIsInstance(self.list, Iterator, "Method iterator() must return ForwardListIterator object.")
        self.assertFalse(self.list.has_next(), "Iterator on empty list must return false for has_next() method.")

    def test_empty_list(self):
        self.assertEqual(self.list.get_size(), 0, "Size of empty list must be 0.")
        self.assertTrue(self.list.is_empty(), "Method isEmpty() must return true for an empty list.")

    def test_remove_from_empty_list(self):
        with self.assertRaises(ValueError, msg="Throw an ValueError if user tries to remove the first element from an empty list."):
            self.list.remove_first()
        with self.assertRaises(ValueError, msg="Throw an ValueError if user tries to remove the last element from an empty list."):
            self.list.remove_last()
    
    def test_get_from_empty_list(self):
        with self.assertRaises(ValueError, msg="Throw an ValueError if user tries to get the first element from an empty list."):
            self.list.get_first()
        with self.assertRaises(ValueError, msg="Throw an ValueError if user tries to get the last element from an empty list."):
            self.list.get_last()
    
    def test_add_one_head(self):
        self.list.add_first("1")

        self.assertEquals("1", self.list.get_first(), "Head must reference inserted element.")
        self.assertEquals("1", self.list.get_last(), "Tail must reference inserted element.")

        self.assertEquals(1, self.list.get_size(), "Size of list must be 1.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 1.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("1", next(self.iter), "Iterator must return inserted element.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

    def test_add_one_tail(self):
        self.list.add_last("1")

        self.assertEquals("1", self.list.get_first(), "Head must reference inserted element.")
        self.assertEquals("1", self.list.get_last(), "Tail must reference inserted element.")

        self.assertEquals(1, self.list.get_size(), "Size of list must be 1.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 1.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("1", next(self.iter), "Iterator must return inserted element.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

    def test_add_two_head(self):
        self.list.add_first("2")
        self.list.add_first("1")

        self.assertEquals("1", self.list.get_first(), "First element in list incorrect.")
        self.assertEquals("2", self.list.get_last(), "Last element in list incorrect.")

        self.assertEquals(2, self.list.get_size(), "Size of list must be 2.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 2.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("1", next(self.iter), "Iterator must return inserted element.")
        self.assertEquals("2", next(self.iter), "Iterator must return inserted element.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

    def test_add_two_tail(self):
        self.list.add_last("1")
        self.list.add_last("2")

        self.assertEquals("1", self.list.get_first(), "First element in list incorrect.")
        self.assertEquals("2", self.list.get_last(), "Last element in list incorrect.")

        self.assertEquals(2, self.list.get_size(), "Size of list must be 2.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 2.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("1", next(self.iter), "Iterator must return inserted element.")
        self.assertEquals("2", next(self.iter), "Iterator must return inserted element.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

    def test_add_three_head(self):
        self.list.add_first("1")
        self.list.add_first("2")
        self.list.add_first("3")

        self.assertEquals("3", self.list.get_first(), "First element in list incorrect.")
        self.assertEquals("1", self.list.get_last(), "Last element in list incorrect.")

        self.assertEquals(3, self.list.get_size(), "Size of list must be 3.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 3.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("3", next(self.iter), "Iterator must return inserted element.")
        self.assertEquals("2", next(self.iter), "Iterator must return inserted element.")
        self.assertEquals("1", next(self.iter), "Iterator must return inserted element.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

    def test_add_three_tail(self):
        self.list.add_last("1")
        self.list.add_last("2")
        self.list.add_last("3")

        self.assertEquals("1", self.list.get_first(), "First element in list incorrect.")
        self.assertEquals("3", self.list.get_last(), "Last element in list incorrect.")

        self.assertEquals(3, self.list.get_size(), "Size of list must be 3.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 3.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("1", next(self.iter), "Iterator must return inserted element.")
        self.assertEquals("2", next(self.iter), "Iterator must return inserted element.")
        self.assertEquals("3", next(self.iter), "Iterator must return inserted element.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

    def test_add_three_remove_from_front(self):
        self.list.add_first("1")
        self.list.add_first("2")
        self.list.add_first("3")

        self.assertEquals("3", self.list.remove_first(), "First element in list incorrect.")

        self.assertEquals(2, self.list.get_size(), "Size of list must be 2.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 2.")
        
        self.assertEquals("2", self.list.get_first(), "First element in list incorrect.")
        self.assertEquals("1", self.list.get_last(), "Last element in list incorrect.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("2", next(self.iter), "First element in list incorrect.")
        self.assertEquals("1", next(self.iter), "Second element in list incorrect.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

        self.assertEquals("2", self.list.remove_first(), "Second element in list incorrect.")
        self.assertEquals("1", self.list.remove_first(), "Third element in list incorrect.")

        self.assertEquals(0, self.list.get_size(), "Size of list must be 0.")
        self.assertTrue(self.list.is_empty(), "Method isEmpty() must return true for an empty list.")

        with self.assertRaises(ValueError, msg="Throw an ValueError if user tries to remove an element from an empty list."):
            self.list.remove_first()

    def test_add_three_remove_from_back(self):
        self.list.add_first("1")
        self.list.add_first("2")
        self.list.add_first("3")

        self.assertEquals("1", self.list.remove_last(), "Last element in list incorrect.")

        self.assertEquals(2, self.list.get_size(), "Size of list must be 2.")
        self.assertFalse(self.list.is_empty(), "Method is_empty() must return false for a list of size 2.")

        self.iter = iter(self.list)
        self.assertTrue(self.iter.has_next(), "Iterator must return true for has_next() method.")
        self.assertEquals("3", next(self.iter), "First element in list incorrect.")
        self.assertEquals("2", next(self.iter), "Second element in list incorrect.")
        self.assertFalse(self.iter.has_next(), "Iterator must return false for has_next() method.")

        self.assertEquals("2", self.list.remove_last(), "Second element in list incorrect.")
        self.assertEquals("3", self.list.remove_last(), "First element in list incorrect.")

        self.assertEquals(0, self.list.get_size(), "Size of list must be 0.")
        self.assertTrue(self.list.is_empty(), "Method isEmpty() must return true for an empty list.")

        with self.assertRaises(ValueError, msg="Throw an ValueError if user tries to remove an element from an empty list."):
            self.list.remove_first()

if __name__ == '__main__':
    unittest.main()
