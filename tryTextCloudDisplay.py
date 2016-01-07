from visual import *
import random

def windowSetup():
    """
    Sets up the VPython window "scene"
    <http://www.vpython.org/webdoc/visual/display.html>
    """
    scene.autoscale = False
    scene.background = color.black
    scene.width = 960
    scene.height = 540
    scene.x = 50
    scene.y = 50
    scene.title = "Text Cloud"

def extreme(wordList, max_min):
    max, min = 0, 0
    for i in range(len(wordList)):
        if wordList[i][1] < wordList[min][1]:
            min = i
        if wordList[i][1] > wordList[max][1]:
            max = i
    return (max if max_min else min)
        

def findHeight(wordList, pos):
    """

    """
    # rangeFreq instead of maxFreq so no word becomes illegible
    rangeFreq = wordList[extreme(wordList,1)][1] - \
                wordList[extreme(wordList,0)][1]
    return (55 * wordList[pos][1])/rangeFreq + 20 # minimum font size = 20
   
def findWidth(wordList, pos):
    """

    """
    try:
        adjustLen = len(wordList[pos][0])
        for char in wordList[pos][0]:
            if char in ['f', 'i', 'j', 'l', 'r', 't']: # short characters
                adjustLen -= 0.5
            elif char in ['m', 'w']: # long characters
                adjustLen += 0.5
        return (0.9 * adjustLen * findHeight(wordList, pos))/ \
               findHeight(wordList, extreme(wordList,1))
    except IndexError: # error handling for last findWidth()
        return 0 

def displayCloud(wordList):
    """

    """
    x, y = -8.5, 5.0
    pos = 0 # number of words added to Text Cloud (current position)
    random.shuffle(wordList)
    
    while pos < len(wordList):
        wordHeight = findHeight(wordList, pos)
        x_ = (findWidth(wordList, pos) + findWidth(wordList, pos+1))/2 + 0.8
        if x + x_ > 10.5:
            x = -8.5
            y -= (25*wordHeight)/scene.height # TBC
        else:
            myLabel = label(text = wordList[pos][0],
                            pos = (x, y, 0),
                            color = color.red,
                            height = wordHeight,
                            box = False,
                            border = 0,
                            font = "helvetica")
            x += x_
            pos += 1

def main():
    """
    Function called at program run
    """
    wordList = [('whale', 1392), ('like', 588), ('man', 537), ('ahab', 498), ('ye', 486), ('sea', 466), ('old', 446), ('time', 436), ('boat', 426), ('captain', 337), ('head', 333), ('hand', 329), ('look', 326), ('long', 324), ('great', 324), ('chapter', 315), ('thing', 312), ('say', 311), ('said', 293), ('way', 278), ('white', 276), ('eye', 268), ('thou', 264), ('stubb', 257), ('round', 256), ('did', 251), ('little', 249), ('day', 248), ('sperm', 241), ('queequeg', 239), ('water', 231), ('men', 230), ('come', 226), ('turn', 213), ('stand', 203), ('good', 203), ('himself', 200), ('know', 194), ('starbuck', 189), ('sail', 186), ('thought', 183), ('let', 183), ('deck', 181), ('world', 177), ('away', 176), ('pequod', 175), ('work', 172), ('ship', 172), ('sort', 171), ('think', 169)]
    windowSetup()
    displayCloud(wordList)
    

if __name__=="__main__":
    main()
