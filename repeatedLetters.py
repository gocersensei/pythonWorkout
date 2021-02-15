from collections import Counter
import operator

WORDS = ['this', 'is', 'an',
         'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    # What letter appears the most times, and how many
    # times does it appear?
    # Counter.most_common returns a list of two-element tuples (value
    # and count) in descending order.
    # Just as you can pass key to sorted, you can
    # also pass it to max and use a different sort method.
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)


print(most_repeating_word(WORDS))