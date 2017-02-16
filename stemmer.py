"""
A modified stemming algorithm based on the renowned Porter Stemming
Algorithm given by Martin Porter.

Refer to:
<http://tartarus.org/~martin/PorterStemmer/>
<http://tartarus.org/~martin/PorterStemmer/python.txt>
"""


class ModifiedStemmer:

    def __init__(self):
        self.w = ''         # word to stem
        self.k = 0          # index of last character

    def update(self):
        """
        Updates the word by chopping off portion of the word
        already determined to be suffixes
        """
        self.w = self.w[:self.k + 1]

    def is_e_restorable(self):
        """
        Determines whether the terminating e character should
        be restored (e.g., structur returns True and self.w
        becomes structure)

        :return True if 'e' should be restored
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        return (self.w[self.k] not in vowels)       \
            and (self.w[self.k - 1] in vowels)      \
            and (self.w[self.k - 2] not in vowels)

    def stem_major(self):
        """
        Converts the word in context to singular and removes
        primary suffixes such as -ed or -ing or -er

        caresses    ->  caress
        ponies      ->  pony
        cats        ->  cat

        meetings    ->  meeting     ->  meet
        number      ->  number
        studied     ->  study
        structured  ->  structur    ->  structure

        spamming    ->  spamm       ->  spam
        spelled     ->  spell
        missing     ->  miss
        """
        if self.w.endswith('s'):
            if self.w.endswith(('sses', 'ies')):
                self.k -= 2
                if self.w.endswith('ies'):
                    self.w = self.w[:self.k] + 'y'
            elif not self.w.endswith('ss'):
                self.k -= 1
            self.update()

        if self.w.endswith(('ed', 'ing', 'er')):
            if self.w.endswith(('ed', 'er')):
                if self.w.endswith('er') and self.w[self.k - 2] != self.w[self.k - 3]:
                    return
                self.k -= 2
                if self.w.endswith('ied'):
                    self.w = self.w[:self.k] + 'y'
                if self.is_e_restorable():
                    self.k += 1
            else:
                self.k -= 3
            if (self.w[self.k] == self.w[self.k - 1])\
                    and (self.w[self.k] not in ['l', 's', 'z']):
                self.k -= 1
            self.update()

    def stem_other(self):
        """
        Removes other major suffixes not accounted for by
        stem_major()

        relational  ->  relation    ->  relate
        conditional ->  condition
        comfortably ->  comfortable ->  comfort
        awkwardly   ->  awkward
        electricity ->  electric
        hopefulness ->  hope
        goodness    ->  good
        enjoyment   ->  enjoy
        richest     ->  rich
        """
        suffixes = [
            ['tional', 'tion'],
            ['ality', 'al'],
            ['able', 'able'],
            ['ably', ''],
            ['ly', ''],
            ['ization', 'ize'],
            ['ation', 'ate'],
            ['icity', 'ic'],
            ['ism', ''],
            ['fulness', ''],
            ['ness', ''],
            ['ive', ''],
            ['ment', ''],
            ['est', ''],
            ['ship', ''],
        ]

        for i in range(len(suffixes)):
            if self.w.endswith(suffixes[i][0]):
                self.w = self.w[:-1 * len(suffixes[i][0])] + suffixes[i][1]

    def stem(self, word_to_stem):
        """
        
        :param word_to_stem: word to stem
        :return stemmed word
        """
        self.w = word_to_stem
        self.k = len(word_to_stem) - 1

        self.stem_major()
        if word_to_stem == self.w:
            self.stem_other()

        return self.w
