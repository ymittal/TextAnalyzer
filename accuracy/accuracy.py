import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from stemmer import ModifiedStemmer

words_to_stem = []
valid_words = []

with open("voc.txt") as fin:
    words_to_stem = fin.read().splitlines()
    
with open("output.txt") as fin:
    valid_words = fin.read().splitlines()
    
s = ModifiedStemmer()
count = 0

for i in range(len(words_to_stem)):
    word = words_to_stem[i]
    if len(word) > 1:
        words_to_stem[i] = s.stem(word)
        if words_to_stem[i] == valid_words[i]:
            count += 1

print ('Accuracy: {0:.4f}%'.format((count * 100.0) / len(valid_words)))
