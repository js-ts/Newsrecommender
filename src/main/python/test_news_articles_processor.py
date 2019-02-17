import unittest
from news_articles_processor import get_tokens
from news_articles_processor import get_nouns


class TestGetToken(unittest.TestCase):

    def test_get_token(self):
        self.assertNotEqual(len(get_tokens('hello world')), 0)

    def test_get_nouns(self):
        self.assertEqual(get_nouns(("Berlin", "NN")), "Berlin")
        #self.assertEqual(get_nouns('car'), 'None')


if __name__ == '__main__':
	unittest.main()