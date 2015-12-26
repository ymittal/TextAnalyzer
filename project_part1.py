from hmc_urllib import getHTML
from simpleTextCloudDisplay import displayCloud
import string

MAX_WORDS = 10

def findMostFrequentList(freqDict):
    freqStr = ""
    freqList = []
    words = list(freqDict.keys())
    frequencies = list(freqDict.values())
    for i in range(0, len(freqDict)):
        freqList.append((frequencies[i],words[i])) # word-frequency order reversed in tuple
    freqList.sort(reverse=True)

    # reversing order again (fix) of first 50 (most frequent words) elements
    for j in range(0,MAX_WORDS):
        freqList[j] = (freqList[j][1], freqList[j][0])
        freqStr += freqList[j][0] + " (" + str(freqList[j][1]) + ") \n"
    print ("\nHere is the text cloud for your web page: \n", freqStr)
    return freqList[0:MAX_WORDS]
    
##    Modified Selection Sort
##    for i in range(0, MAX_WORDS):
##        max = i
##        for j in range(i+1,len(words)):
##            if frequencies[j] > frequencies[max]:
##                max = j
##        words[i], words[max] = words[max], words[i]
##        frequencies[i], frequencies[max] = frequencies[max], frequencies[i]
##        freqStr += words[i] + " (" + str(frequencies[i]) + ")\n"
##    print ("\nHere is the text cloud for your web page: \n", freqStr)
##    return freqStr

def findFrequency(finalWords):
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
    # stop-words.txt: <http://xpo6.com/list-of-english-stop-words/>
    stopwords = []
    with open("stop-words.txt") as fin:
        stopwords = fin.read().splitlines()
    
    cleanContent(wordList, stopwords)
    stemContent(wordList)
    return wordList

def getContent():
    url = input('Please enter a URL ')
    if "://" not in url:
        url = "http://" + url
    contents = getHTML(url) # returns a tuple(content,urls)
    return contents[0].split()  # contents[0] = website text

def main():
    """
    Function called at program run
    """
    wordList = getContent()
    finalWords = filterContent(wordList)
    freqDict = findFrequency(finalWords)
    freqList = findMostFrequentList(freqDict)
    displayCloud(freqList)
    
if __name__=="__main__":
    main()
