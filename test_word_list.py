"""Tests for WordList — Bug Finding phase."""

import unittest

from word_list import WordList


class WordListTest(unittest.TestCase):

    def test_word_count(self) -> None:
        wl = WordList(["apple", "banana", "cherry"])
        self.assertEqual(wl.word_count(), 3)

    def test_removes_duplicates(self) -> None:
        wl = WordList(["apple", "apple", "banana"])
        self.assertEqual(wl.word_count(), 2)

    def test_contains_basic(self) -> None:
        wl = WordList([])
        self.assertTrue(wl.contains_as_substring("apple", "app"))
        self.assertTrue(wl.contains_as_substring("banana", "nana"))
        self.assertFalse(wl.contains_as_substring("cat", "dog"))

    def test_contains_at_different_positions(self) -> None:
        wl = WordList([])
        self.assertTrue(wl.contains_as_substring("hello", "he"))
        self.assertTrue(wl.contains_as_substring("hello", "lo"))
        self.assertTrue(wl.contains_as_substring("hello", "ell"))

    def test_contains_same_word(self) -> None:
        wl = WordList([])
        self.assertEqual(wl.contains_as_substring("apple", "apple"), False)

    def test_contains_longer_word(self) -> None:
        wl = WordList([])
        self.assertEqual(wl.contains_as_substring("app", "apple"), False)

    def test_valid_word_normal(self) -> None:
        wl = WordList([])
        self.assertEqual(wl.is_valid_word("hello"), True)

    def test_valid_word_spaces(self) -> None:
        wl = WordList([])
        self.assertEqual(wl.is_valid_word("hello world"), False)

if __name__ == "__main__":
    unittest.main()
