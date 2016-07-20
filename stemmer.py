"""
Modified Porter Stemming Algorithm to remove
frequently occuring suffixes

References:
<http://tartarus.org/~martin/PorterStemmer/>
<http://tartarus.org/~martin/PorterStemmer/python.txt>
"""

class ModifiedStemmer:
    
    def __init__(self):
        self.w = '' # copy of word to be stemmed (Class Scope)
        self.k = 0  # decreases as stemming progresses (changed only if needed)
                    # holds index of last character

    def update(self):
        """
        Updates self.w (deletes found suffixes) 
        """
        self.w = self.w[ :self.k+1]

    def isRestorable(self):
        """
        Returns True if 'e' should be restored
        (e.g., structur -> returns True -> structure)
        """
        vowels = ['a','e','i','o','u']
        return (self.w[self.k] not in vowels)\
                   and (self.w[self.k-1] in vowels)\
                   and (self.w[self.k-2] not in vowels)
        
    def stemMajor(self):
        """
        Removes plurals and -ed or -ing or -er. e.g.

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
                    self.w = self.w[ :self.k] + 'y'
            elif not self.w.endswith('ss'):
                self.k -= 1
            self.update()
            
        if self.w.endswith(('ed','ing','er')):
            if self.w.endswith(('ed','er')):
                if self.w.endswith('er') and self.w[self.k-2] != self.w[self.k-3]:
                    return
                self.k -= 2
                if self.w.endswith('ied'):
                    self.w = self.w[ :self.k] + 'y'
                if self.isRestorable():
                    self.k += 1
            else:
                self.k -= 3
            if (self.w[self.k] == self.w[self.k-1])\
                   and (self.w[self.k] not in ['l','s','z']):
                self.k -= 1
            self.update()
        return self.w

    def stemOther(self):
        """
        Removes major suffixes not addressed previously. e.g.

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
        suffix = ['tional', 'ality', 'able','ably', 'ly',
                  'ization', 'ation', 'icity', 'ism',
                  'fulness','ness', 'ive','ment','est','ship']
        changeTo = ['tion', 'al', 'able', '','',
                    'ize', 'ate', 'ic', '', '',
                    '', '', '', '', '']

        for i in range(len(suffix)):
            if self.w.endswith(suffix[i]):
                self.w = self.w[ :-1*len(suffix[i])] + changeTo[i]
        return self.w
    
    def stem(self, word):
        """
        Calls stemMajor() and stemOther(), returns the stemmed word
        """
        self.w = word
        self.k = len(word)-1
        
        # usually changes, if any, after stemMajor() are the only ones
        if word != self.stemMajor():
            return self.w
        return self.stemOther()
