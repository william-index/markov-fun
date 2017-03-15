import attr, re

@attr.s
class DataTrainer(object):

    """
    Trains a markov model of a given order off a given text file.

    Args:
        filename (string) : path to file from project root
        order (int) : depth of words/tokens to construct keys from
    Returns:
        Dict: trained markov model
    """
    def train_text_data(self, raw_text, order):
        cleaned_text = self.strip_special_chars(raw_text)
        data = self.crawl_clean_text(text=cleaned_text, order=order)

        return data

    """
    Strips out special characters except select punctuation and indicates EOL in
    place of said select punctuation.

    Args:
        data (string) : raw text data
    Returns:
        string: alpha-numeric and spaces only string with ".", "!", and "?"
                replaced by "EOL"
    """
    def strip_special_chars(self, data):
        cleaned_text = re.sub('!|\.|\?', ' EOL ', data)
        cleaned_text = re.sub('[^A-Za-z0-9\s\'-]+', ' ', cleaned_text)
        cleaned_text = re.sub( '\s+', ' ', cleaned_text).strip()
        return cleaned_text

    """
    Splits a string by spaces and creates a dict of lists for all possibilities
    of N order.

    Args:
        test (string) : string of text
        order (int) : depth of words/tokens to construct keys from
    Returns:
        Dict: Dict of lists for all n Order keys and all possibilities
    """
    def crawl_clean_text(self, text, order):
        text_seq = text.split()
        tree = {}

        for i in range(0, len(text_seq) - order):
            key = ""
            for j in range(0, order):
                key = key + " " + text_seq[i+j]
            key = key[1:]

            if not key in tree:
                tree[key] = []

            tree[key].append(text_seq[i + order])

        return tree
