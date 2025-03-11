import unittest
from Prog import WordCounter
class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.word_counter = WordCounter()
    
    def test_empty_string(self):
        self.assertEqual(WordCounter.count_words(""), 0)

    def test_one_word(self):
        self.assertEqual(WordCounter.count_words("word"), 1)

    def test_more_words(self):
        self.assertEqual(WordCounter.count_words("Это строка с пятью словами"), 5)

    def test_more_spaces(self):
        self.assertEqual(WordCounter.count_words("   много пробелов  "), 2)

    def test_more_spaces_between_words(self):
        self.assertEqual(WordCounter.count_words("много   пробелов между   словами"), 4)

    def test_newline(self):
        self.assertEqual(WordCounter.count_words("строка\nс\nновыми\nстроками"), 4)

    def test_tabs(self):
        self.assertEqual(WordCounter.count_words("слово\tслово\tслово"), 3)

    def test_only_spaces(self):
        self.assertEqual(WordCounter.count_words("     "), 0)

    def test_special_char(self):
        self.assertEqual(WordCounter.count_words("!@#$%^&*()"), 1)

    def test_num_string(self):
        self.assertEqual(WordCounter.count_words("123 456 789"), 3)

if __name__ == "__main__":
    unittest.main()