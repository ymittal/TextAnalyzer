class ModifiedStemmer:
    def __init__(self):
        self.w = ''
        self.k = 0

    def update(self): # delete "determined" suffix
        self.w = self.w[ :self.k+1]

    def isRestorable(self): # check is 'e' can be restored
        vowels = ['a','e','i','o','u']
        return (self.w[self.k] not in vowels)\
                   and (self.w[self.k-1] in vowels)\
                   and (self.w[self.k-2] not in vowels)
        
    def stemMajor(self):
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

    def stemOther(self):
        suffix = ['tional', 'ality', 'ably', 'ly', 'ization',
                  'ation', 'icity', 'ism', 'fulness','ness','able'
                  'ive','ment','est','ship']
        changeTo = ['tion', 'al', 'able', '', 'ize', 'ate', 'ic',
                    '', '','','','','','','']
        for i in range(len(suffix)):
            if self.w.endswith(suffix[i]):
                self.w = self.w[ :-1*len(suffix[i])] + changeTo[i]
                self.k += len(changeTo[i]) - len(suffix[i])
    
    def stem(self, word):
        self.w = word
        self.k = len(word)-1
        self.stemMajor()
        if word != self.w:
            return self.w
        self.stemOther()
        return self.w

def main():
    s = Stemmer()
    wordList = ['caresses','ponies','structured','spelled',
                'studied','spamming','spammed','missing','able']
    wordList = ['relational','conditional','valency','comfortably',
                'differently','victimization','communalism','hopefulness',
                'formality','electricity','goodness','number','jogger']
    exceptions = {}
    for i in range(len(wordList)):
        word = wordList[i]
        if len(word) > 1:
            if word not in exceptions:
                wordList[i] = s.stem(word)
            else:
                wordList[i] = exceptions[word]
    print (wordList)
    
if __name__=='__main__':
    main()
