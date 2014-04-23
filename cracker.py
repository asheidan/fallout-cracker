#!/usr/bin/env python3

import sys
from collections import defaultdict
import cmd
from pprint import pprint


wordlist = []
words = []
word_length = 0


def hori_line():
    print("-" * (word_length + 2), "+", "-" * (3 * len(wordlist)), "--+", sep='')


for filename in sys.argv[1:]:
    with open(filename, "r") as inputfile:
        wordlist += [s.strip() for s in inputfile.readlines()]

word_length = len(wordlist[0])

# print("Word: ", end='', file=sys.stderr)
#word = sys.stdin.readline().strip()

# Print vertical

for i in range(0, len(wordlist[0])):
    print(" " * (word_length + 2), "|", sep='', end='')
    for word in wordlist:
        print(" %2s" % word[i], end='')

    print("  |")

hori_line()

max_chars = 0
max_char_word = None

frequency_tree = defaultdict(lambda : defaultdict(list))

for a_word in wordlist:
    print(" %s |" % a_word, end='')

    node = frequency_tree[a_word]

    sum_common = 0

    for b_word in wordlist:

        common_characters = 0
        if a_word is not b_word:
            for a, b in zip(a_word, b_word):
                if a == b:
                    common_characters += 1

            freq_list = node[common_characters]
            freq_list.append(b_word)

            sum_common += common_characters
            print(" %2d" % common_characters, end='')
        else:
            print("  -", end='')

    print("  | %2d" % sum_common)

    if (max_chars < sum_common):
        max_chars = sum_common
        max_char_word = a_word

hori_line()

print("Probably best word: %s (%d)" % (max_char_word, max_chars))

print("-------" * word_length + "-----+")

class AIShell(cmd.Cmd):
    intro = "ROBCO INDUSTRIES (TM) TERMLINK HACKER"
    prompt = "> "

    guessed_words = []
    current_word = None

    def emptyline(self):
        sys.exit(0)

    def default(self, line):
        if 'EOF' == line:
            print()
            sys.exit(0)

        try:
            n = int(line)
            pair = (self.current_word, n)
            self.guessed_words.append(pair)
            #pprint(self.guessed_words)
            print("Guess has %d number of characters in common with correct choice" % n)
            #print("Added %s (%d) as guessed word" % pair)

            possible_words = set(wordlist)
            for word, count in self.guessed_words:
                possible_words &= set(frequency_tree[word][count])
                print("%s have %d in common with %s" %
                    (possible_words, count, word))
        except ValueError:
            self.current_word = line.strip()
            print("Guessed on the word %s" % self.current_word)

#pprint(frequency_tree[max_char_word])

guessed_words = []
current_word = max_char_word

AIShell().cmdloop()
