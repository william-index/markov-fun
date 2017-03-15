import unittest, mock
from Trainer import DataTrainer

class TestDataTrainer(unittest.TestCase):
    """
    Runs setup for each test no matter what
    """
    def setUp(self):
        super(TestDataTrainer, self).setUp() #calls setUp on parent

        self.trainer  = DataTrainer()

        self.sample_data = """
            Some, sentences "end-with". (Some sentences) might end with!
            But we don't know, other sentences might end with?
        """

        self.stripped_data = "Some sentences end-with EOL Some sentences might end with EOL But we don't know other sentences might end with EOL"

        self.expected_tree = {
            'But we': ["don't"],
            'EOL But': ['we'],
            'EOL Some': ['sentences'],
            'Some sentences': ['end-with', 'might'],
            "don't know": ['other'],
            'end with': ['EOL', 'EOL'],
            'end-with EOL': ['Some'],
            'know other': ['sentences'],
            'might end': ['with', 'with'],
            'other sentences': ['might'],
            'sentences end-with': ['EOL'],
            'sentences might': ['end', 'end'],
            "we don't": ['know'],
            'with EOL': ['But']}


    def test_train_text_data(self):
        result = self.trainer.train_text_data(self.sample_data, 2)
        expected = self.expected_tree

        self.assertDictEqual(expected, result)


    def test_strip_special_chars(self):
        result = self.trainer.strip_special_chars(self.sample_data)
        expected = self.stripped_data

        self.assertEqual(expected, result)


    def test_crawl_clean_text(self):
        result = self.trainer.crawl_clean_text(self.stripped_data, 2)
        expected = self.expected_tree

        self.assertDictEqual(expected, result)
