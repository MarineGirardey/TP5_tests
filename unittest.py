#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:49:42 2021

@author: Marine Girardey
"""
import unittest
from linkedlist_tp_unittest import LinkedList, Node

class RandomTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module 'random'."""

    def set_up(self):
        """Initialisation des tests."""
        self.list = LinkedList(["m", "a", "r", "i", "n", "e"]) # Yes I am egocentric
        self.empty_list = LinkedList([])

    def test_empty_list(self):
        """test if list is empty."""
        self.assertIsNone(self.empty_list.head)

    def test_add_elem_to_list(self):
        """If add element to list, test that it is not empty."""
        self.empty_list.add_first(Node("h"))
        self.assertIsNotNone(self.empty_list.head)

    def test_pile_depile(self):
        """Test if a list after pile and depile is unchanged."""
        list_before = self.list
        self.list.add_after("e", Node("s"))
        self.list.remove_node("s")
        list_after = self.list
        self.assertEqual(list_before, list_after)

    def test_content_pile_elem(self):
        """Test if the r added to the list is r"""
        self.list.add_after("e", Node("r"))
        last_elem = str(self.list.get(6))
        self.assertEqual(last_elem, "r")

if __name__ == '__main__':
    unittest.main()
