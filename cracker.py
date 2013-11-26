#!/usr/bin/env python3

import sys


wordlist_file = sys.argv[1]
wordlist = []
words = []
word_length = 0


def hori_line():
    print("-" * (word_length + 2), "+", "-" * (3 * len(wordlist)), "--+", sep='')


with open(wordlist_file, "r") as file:
    wordlist = [s.strip() for s in file.readlines()]

word_length = len(wordlist[0])

# print("Word: ", end='', file=sys.stderr)
#word = sys.stdin.readline().strip()

# Print vertical

for i in range(0, len(wordlist[0])):
    print(" " * (word_length + 2), "|", sep='', end='', file=sys.stderr)
    for word in wordlist:
        print(" %2s" % word[i], end='', file=sys.stderr)

    print("  |", file=sys.stderr)

hori_line()

for a_word in wordlist:
    print(" %s |" % a_word, end='', file=sys.stderr)

    sum_common = 0

    for b_word in wordlist:

        common_characters = 0
        if a_word is not b_word:
            for a, b in zip(a_word, b_word):
                if a == b:
                    common_characters += 1

            sum_common += common_characters
            print(" %2d" % common_characters, end='', file=sys.stderr)
        else:
            print("  -", end='', file=sys.stderr)

    print("  | %2d" % sum_common, file=sys.stderr)

hori_line()
