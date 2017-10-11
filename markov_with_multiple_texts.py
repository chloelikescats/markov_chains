"""Generate Markov text from text files. Insert n gram length, then any text files 
to draw from"""

from random import choice
import string
import sys


def open_and_read_file(input_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    full_text = ""
    for i in range(len(input_path)):
        with open(input_path[i]) as the_file:
            the_file = the_file.read()
            full_text = full_text + the_file

    return full_text


def make_chains(text_string, n_gram_size):
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
    #so we know when to end:
    # list_of_words.append(None) #adds none to end of list so it will be last in last key
    chains = {}

    # for word in list_of_words:
    key = tuple(list_of_words[0:n_gram_size])
    value = list_of_words[n_gram_size + 1]
    chains[key] = [value]

    #using i and n_gram_size to incriment through list and get keys
    for i in range(1, len(list_of_words) - n_gram_size):
        key = []
        key = tuple(list_of_words[i:n_gram_size + i])

        value = list_of_words[n_gram_size + i]
        #if key exists, awesome; else, make [] value:
        chains.setdefault(key, [])
        chains[key].append(value)

    # print chains
    return chains


def make_text(chains, n_gram_size):
    """Return text from chains."""

    words = []

    key = choice(chains.keys())
    ###Choosing length of key
    words.extend(key)
    #capitalize beginning of poem
    words[0] = words[0].title()

    while True:
        # import pdb; pdb.set_trace()
        # if it hits end of doc or 140 characters, stop

        if len(words) >= 140 or (not key in chains):
            words.append("\n")
            break
        #figure out why it ends abruptly, make it elif
        #elif
        else:
            # print chains
            new_word = choice(chains[key])
            words.append(new_word)

            #get new key with last n_gram_size elements of words list
            key = words[-n_gram_size:]
            key = tuple(key)

            #make it break at any punctuation
            for i in range(len(words)):
                if words[i][-1] in string.punctuation:

                    #ignore commas but break at all OTHER punc
                    if not words[i][-1] == ",":
                        break
    #make line breaks at punctuation
    for i in range(len(words)):
        if words[i][-1] in string.punctuation and words[i][-1] != ',':
            words[i + 1: i + 1] = '\n'

    ####format for twitter#####
    full_string = " ".join(words)

    twitter_length_string = full_string[:141]
    #find last punctuation before twitter limit; return pretty tweet
    for i in range(-1, -len(twitter_length_string), -1):
        if twitter_length_string[i] in set(['.', '?', '!']):
            return twitter_length_string[:i + 1]


def validate_n_gram_amount(input_text):
    """gets user input, returns int if int can be used as n gram"""
    while True:
        #user input is now the entered on command line
        user_input = sys.argv[1]
        # user_input = raw_input("How many words in n_gram? > ") #old version
        try:
            user_input = int(user_input)
        except:
            print "Please enter a valid input"
            continue
        if 1 < user_input < len(input_text.split()):
            return user_input
        else:
            length = str(len(input_text.split()))
            print "Please input a number less than %s" % (length)


input_path = sys.argv[2:]
open_and_read_file(input_path)

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

#get n_gram size from user
n_gram_size = validate_n_gram_amount(input_text)

# Get a Markov chain
chains = make_chains(input_text, n_gram_size)

# Produce random text
random_text = make_text(chains, n_gram_size)


print random_text
