from hmc_urllib import getHTML
from complexTextCloudDisplay import displayCloud
from modifiedStemmer import ModifiedStemmer
import string

MAX_WORDS = 50

def findMostFrequentList(freqDict):
    """
    Param(s): freqDict -> Dict of word-frequency pairs
    Finds (MAX_WORDS) most frequent words using List.sort(),
    adds word-frequency pairs to freqStr in required format
    Returns as a List tuples (word, frequency) in DESC order of frequency
    <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>
    <https://docs.python.org/2/tutorial/datastructures.html#more-on-lists>
    """
    """
    findMostFrequentList({'test': 2, 'random': 10, 'max': 100, 'testify': 2, 'min': 1})
    findMostFrequentList({'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
                          'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
                          'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'aa':27, 'ab':28, 'ac':29, 'ad':30,
                          'ae':31, 'af':32, 'ag':33, 'ah':34, 'ai':35, 'aj':36, 'ak':37, 'al':38, 'am':39, 'an':40,
                          'ao':41, 'ap':42, 'aq':43, 'ar':44, 'as':45, 'at':46, 'au':47, 'av':48, 'aw':49, 'ax':50,
                          'ay':51, 'az':52})
    """
    # Inspiration from <http://bit.do/StackOverflow-Global2Local>
    MAX_WORDS = globals()['MAX_WORDS']  # so global MAX_WORDS is not modified
    freqStr = ""
    freqList = []
    words = list(freqDict.keys())
    frequencies = list(freqDict.values())
    for i in range(0, len(freqDict)):
        freqList.append((frequencies[i],words[i])) # word-frequency order reversed in tuple
    freqList.sort(reverse=True)
           
    if len(freqList) < MAX_WORDS:
        MAX_WORDS = len(freqList) # prevents IndexError

    # reversing order again (fix) of first 50 (most frequent words) elements    
    for j in range(0,MAX_WORDS):
        freqList[j] = (freqList[j][1], freqList[j][0])
        freqStr += freqList[j][0] + " (" + str(freqList[j][1]) + ") \n"
    print ("\nHere is the text cloud for your web page: \n", freqStr)
    return freqList[0:MAX_WORDS]

def findFrequency(finalWords):
    """
    Param(s): finalWords -> List of cleaned and stemmed words
    Returns as a Dict of word-frequency pairs
    """
    """
    findFrequency(['','test','','testify','test','','testify'])
    """
    freqDict = {}
    for word in finalWords:
        if len(word) > 0:   # ignores stray spaces (e.g., Moby Dick's story webpage)
            if word not in freqDict:
                freqDict[word] = 1
            else:
                freqDict[word] += 1
    print ("\nHere is the dictionary of words on that page: \n", freqDict)
    return freqDict
    
def cleanContent(wordList, stopwords):
    """
    Param(s): wordList -> List of words on website entered
              stopwords -> List of stopwords
    Removes punctuation marks (string.punctuation) and digits
    using string.replace method, checks (and deletes) stopwords
    Returns as a List cleaned words
    <https://docs.python.org/2/library/string.html> | Stack Overflow
    """
    """
    cleanContent(['test1','te.st','','a1'], ['','a'])
    cleanContent(['te.st1','other'], ['other'])
    """
    stopwordsIndices = []
    strangeCharacters = string.punctuation + '0123456789'
    for i in range(len(wordList)):
        for character in strangeCharacters:
            wordList[i] = wordList[i].replace(character,"")
        if wordList[i] in stopwords:
            stopwordsIndices.insert(0,i) # cannot append as deletion would throw IndexError
    
    for index in stopwordsIndices:
        del wordList[index] # deletes stopwords from Right to Left

def stemContent(wordList):
    """
    Param(s): wordList -> List of clean words (no punctuation or stopwords)
    Stems words (usually, suffixed words) into root word
    Returns as a List stemmed words
    """
    """
    stemContent(['jog','jogs','jogging','jogged','jogger'])
    stemContent(['caresses','ponies','structured','spelled','studied',
                 'spamming','spammed','missing','able'])
    """
    s = ModifiedStemmer()
    exceptions = {}
    for i in range(len(wordList)):
        word = wordList[i]
        if len(word) > 1: # extra short words are neglected
            if word not in exceptions:
                wordList[i] = s.stem(word)
            else:
                wordList[i] = exceptions[word]

def filterContent(wordList):
    """
    Param(s): wordList -> List of all words on entered website
    Calls helper functions to "clean" and "stem" words
    Returns as a List pure words (no punctuation, stop-words or stemmed words)
    """
    """
    filterContent(['rel(a)tional','conditional','comfortably','differently',
                   'this.1','communal-ism','number1','formality',
                   'electricity','goodness',''])
    """
    # stop-words.txt: <http://xpo6.com/list-of-english-stop-words/>
    stopwords = []
    with open("stop-words.txt") as fin:
        stopwords = fin.read().splitlines()
    
    cleanContent(wordList, stopwords)
    stemContent(wordList)
    return wordList

def getContent(url):
    """
    Param(s): url -> user-entered website
    Returns as a List "splitted" words on the user-entered website
    """
    """
    getContent("http://www.eg.bucknell.edu/~csci203/placement/2016-spring/project/page1.html")
    getContent("www.eg.bucknell.edu/~csci203/placement/2016-spring/project/page1.html")
    """
    if "://" not in url:
        url = "http://" + url
    contents = getHTML(url) # returns a tuple(content,urls)
    return contents[0].split()  # contents[0] = website text

def main():
    """
    Function called at program run
    """
    url = input('Please enter a URL ')
    wordList = getContent(url)
    finalWords = filterContent(wordList)
    freqDict = findFrequency(finalWords)
    freqList = findMostFrequentList(freqDict)
    # displayCloud(freqList)
    
if __name__=="__main__":
    main()
