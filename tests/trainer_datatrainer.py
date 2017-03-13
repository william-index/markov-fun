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
            Some, sentences "end—with". (Some sentences) might end with!
            But we don't know, other sentences might end with?
        """

        self.stripped_data = "Some sentences end with EOL Some sentences might end with EOL But we don't know other sentences might end with EOL"

        self.expected_tree = {
                    'Some sentences': ['end', 'might'],
                    'sentences end': ['with'],
                    'end with': ['EOL', 'EOL', 'EOL'],
                    'with EOL': ['Some', 'But'],
                    'EOL Some': ['sentences'],
                    'sentences might': ['end', 'end'],
                    'might end': ['with', 'with'],
                    'EOL But': ['we'],
                    'But we': ["don't"],
                    "we don't": ['know'],
                    "don't know": ['other'],
                    'know other': ['sentences'],
                    'other sentences': ['might']}


    @mock.patch('Trainer.DataTrainer.get_raw_file_data') # decorator to inject into filesystem where we care about it
    def test_train_text_data(self, get_raw_file_data_mock):
        get_raw_file_data_mock.return_value = self.sample_data

        result = self.trainer.train_text_data('mock.txt', 2)
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
