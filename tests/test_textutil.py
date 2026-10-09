import unittest

from textutil import char_count, word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two  three"), 3)

    def test_empty(self):
        self.assertEqual(word_count(""), 0)


class CharCountTest(unittest.TestCase):
    def test_counts_characters_including_spaces(self):
        self.assertEqual(char_count("one two"), 7)

    def test_counts_characters_excluding_spaces(self):
        self.assertEqual(char_count("one two", include_spaces=False), 6)

    def test_empty(self):
        self.assertEqual(char_count(""), 0)
        self.assertEqual(char_count("", include_spaces=False), 0)


if __name__ == "__main__":
    unittest.main()
