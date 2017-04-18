import sys
from os import path
from nltk.corpus import words
import enchant

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from stemmer import ModifiedStemmer

words_to_stem = []
valid_words = []

with open("input.txt") as fin:
    words_to_stem = fin.read().splitlines()

with open("porter_output.txt") as fin:
    valid_words = fin.read().splitlines()

words = set(words.words())
d = enchant.Dict("en_US")

s = ModifiedStemmer()
count = 0
invalid = 0

for i in range(len(words_to_stem)):
    word_to_stem = words_to_stem[i]
    stemmed_word = s.stem(word_to_stem)

    if not d.check(word_to_stem):  # exclude invalid words to stem
        invalid += 1
        continue

    try:
        if d.check(stemmed_word):
            count += 1
    except:
        pass

print ('Accuracy: {0:.4f}%'.format((count * 100.0) /
                                   (len(valid_words) - invalid)))
