"""Generate Markov text from text files."""

from random import choice
import string


def open_and_read_file(input_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(input_path) as the_file:
        the_file = the_file.read()

    return the_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    list_of_words = text_string.split()
    list_of_words.append(None)
    chains = {}

    # n = 0
    # for word in list_of_words:

    for i in range(len(list_of_words) - 2):
        key = tuple((list_of_words[i], list_of_words[i + 1]))
        value = list_of_words[i + 2]
        chains.setdefault(key, [])
        chains[key].append(value)

    # print chains
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    new_key = choice(chains.keys())
    #append words from tup into words
    words.extend([new_key[0], new_key[1]])

    # options_at_random_thing = chains[random_thing]
    # random_word = choice(options_at_random_thing)
    # words.append(random_word)

    while True:
        if None in chains[new_key]:
            break
        else:
            words.append(choice(chains[new_key]))
            new_key = (words[-2], words[-1])
    #make line breaks at punctuation
    for i in range(len(words)):
        if words[i][-1] in string.punctuation:
            words[i + 1: i + 1] = '\n'


    # words.append(choice(chains[random_thing].values())) #append following words
    # print words

    return " ".join(words)


input_path = "green-eggs.txt"
open_and_read_file(input_path)

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
