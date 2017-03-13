import attr, random, re

@attr.s
class Stepper(object):
    """
    Creates a new phrase for a given model with a given string key for eol. EOL
    will be stripped with the final one being replaced by a randomly select
    string from punc.

    Args:
        model (Dict): trained markov model with expanded option lists
        eol (string): string to indicate end of line
        punc (List): list of strings to be used in place of EOL
    Return:
        string: A complete phrase constructed from the model
    """
    def new_phrase(self, model, eol, punc):
        # all random bits are best done as functions so I can mock them
        start_key = random.choice(list(model.keys()))
        phrase = start_key

        prev_words = start_key.split()
        next_word = ''
        while next_word != eol:
            next_word = self.step(model, ' '.join(prev_words))
            prev_words.pop(0)
            prev_words.append(next_word)

            phrase += ' ' + next_word

        return self.sentencize_phrase(phrase, eol, punc)

    """
    Prettifies the phrase.

    Args:
        phrase (string): a generated phrase
        eol (string): string to indicate end of line
        punc (List): list of strings to be used in place of EOL
    Return:
        string: the input phrase with punctuation and the sentence case
    """
    def sentencize_phrase(self, phrase, eol, punc):
        chosen_punc = random.choice(punc)
        phrase = phrase.split(' ' + eol)
        punctuated_phrase = chosen_punc.join(phrase)

        punctuated_phrase = re.sub(eol+'\s', '', punctuated_phrase)
        capitalized_phrase = punctuated_phrase.title()[0] + punctuated_phrase[1:]

        return capitalized_phrase

    """
    Selects the next token for the phrase.

    Args:
        model (Dict): trained markov model with expanded option lists
        key (string): key for the previous segment of tokens
    Return:
        string: the next word to be used in the phrase
    """
    def step(self, model, key):
        return random.choice(list(model[key]))
