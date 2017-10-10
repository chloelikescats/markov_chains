"""Generate Markov text from text files."""

from random import choice


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
    chains = {}
    list_of_tuples = []
    #create list of all words
    list_of_words = text_string.split()

    n = 0
    for word in list_of_words:
        if n < len(list_of_words) - 1:
            list_of_tuples.append(tuple((list_of_words[n], list_of_words[n + 1])))
            n += 1
        else:
            break

    # make all tuples keys in dictionary
    for item in list_of_tuples:
        chains[item] = []

    # add following words as values to keys in dictionary
    for key in chains:
        n = 0
        for item in list_of_tuples:
            if n < len(list_of_tuples) - 1:
                if item == key:
                    chains[key].append(list_of_tuples[n + 1][1])
                    n += 1
                else:
                    n += 1



    return chains

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

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
