# Dummy URL: http://www.eg.bucknell.edu/~csci203/placement/2016-spring/project/page1.html

from hmc_urllib import getHTML
from simpleTextCloudDisplay import displayCloud
import string

MAX_WORDS = 50
DEPTH = 2

def findMostFrequentList(freqDict):
    """
    Param(s): Dict of word-frequency pairs
    Finds (MAX_WORDS) most frequent words using List.sort(),
    adds word-frequency pairs to freqStr in required format
    Returns as a List tuples (word, frequency) in DESC order of frequency
    <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>
    <https://docs.python.org/2/tutorial/datastructures.html#more-on-lists>
    """
    global MAX_WORDS
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
    return freqList[0:MAX_WORDS]

def findFrequency(finalWords):
    """
    Param(s): finalWords -> List of cleaned and stemmed words
    Returns as a Dict of word-frequency pairs
    """
    freqDict = {}
    for word in finalWords:
        if len(word) > 0:   # ignores stray spaces (e.g., Moby Dick's story webpage)
            if word not in freqDict:
                freqDict[word] = 1
            else:
                freqDict[word] += 1
    return freqDict
    
def cleanContent(wordList, stopwords):
    """
    Param(s): wordList -> List of words on entered website
              stopwords -> List of stopwords
    Removes punctuation marks (string.punctuation) and digits
    using string.replace method, checks (and deletes) stopwords
    Returns as a List "clean" words
    <https://docs.python.org/2/library/string.html> | Stack Overflow
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
    Returns as a List cleaned and stemmed words
    """
    # popular suffixes: <http://www.darke.k12.oh.us/curriculum/la/suffixes.pdf>
    suffixes = ['s','es','ed','ing','ly','er','est','able','ness','ment','ful',
                'less','ship','ish','like','most','ward','wise','ism','some']
    for i in range(len(wordList)):
        word = wordList[i]
        for suffix in suffixes:
            if suffix == word[len(word)-len(suffix): ]:
                word = word[ :-1*len(suffix)]   # removes major suffix
                # usually a trailing character exists (e.g., jogging -> jogg)
                try:
                    if word[-1] == word[-2]:
                        word = word[ :len(word)-1]
                except IndexError:
                    pass
            wordList[i] = word

def filterContent(wordList):
    """
    Param(s): List of words on all pages crawled
    Calls helper functions to "clean" and "stem" words
    Returns as a List pure words (no stop-words or stemmed words)
    """
    # stop-words.txt: <http://xpo6.com/list-of-english-stop-words/>
    stopwords = []
    with open("stop-words.txt") as fin:
        stopwords = fin.read().splitlines()

    cleanContent(wordList, stopwords)
    stemContent(wordList)
    return wordList

def getContent():
    """
    Param(s): None
    Returns as a List "splitted" words on all web pages
    crawled according to set DEPTH
    """
    url = input('Please enter a URL ')
    if "://" not in url:
        url = "http://" + url

    # learned web crawling method in CS101: Building a Search Engine
    # online course on Udacity.com
    uncrawled, crawled, nextLevel = [url], [], []
    depth = 0
    text = ""
    while depth <= DEPTH and uncrawled:
        page = uncrawled.pop()
        if page not in crawled:
            contents = getHTML(page) # returns a tuple(content,urls)
            for link in contents[1]:
                if link not in crawled and link != "http://www.bucknell.edu/":
                    nextLevel.append(link)
            crawled.append(page)
            text += contents[0]
        if uncrawled == []: # increase depth only when all pages on a depth are crawled
            uncrawled, nextLevel = nextLevel, []
            depth += 1
    return text.split()

def main():
    """
    Function called at program run
    """  
    wordList = getContent()
    finalWords = filterContent(wordList)
    freqDict = findFrequency(finalWords)
    freqList = findMostFrequentList(freqDict)
    print (freqList)
    displayCloud(freqList)

if __name__=="__main__":
    main()