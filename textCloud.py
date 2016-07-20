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

def extreme(freqList, max_min):
    """
    Param(s): freqList -> Lists of ordered tuples (word, frequency)
              max_min -> Boolean to determine which extremum to return
    Returns max freq position if max_min is 1, otherwise min freq position
    Note: After freqList is shuffled, extreme values are longer
    directly accessible. This method is implemented to avoid global values
    """
    max, min = 0, 0
    for i in range(len(freqList)):
        if freqList[i][1] < freqList[min][1]:
            min = i
        if freqList[i][1] > freqList[max][1]:
            max = i
    return (max if max_min else min)
        

def findHeight(freqList, pos):
    """
    Param(s): freqList -> Lists of ordered tuples (word, frequency)
              pos -> number of words already added (current position)
    Returns height (font size) of word on position pos
    """
    # rangeFreq instead of maxFreq so no word becomes illegible
    rangeFreq = freqList[extreme(freqList,1)][1] - \
                freqList[extreme(freqList,0)][1]
    return (55 * freqList[pos][1])/rangeFreq + 20 # minimum font size = 20
   
def findWidth(freqList, pos):
    """
    Param(s): freqList -> Lists of ordered tuples (word, frequency)
              pos -> number of words already added (current position)
    Returns approximate "screen width of word" on position pos
    """
    try:
        adjustLen = len(freqList[pos][0])
        for char in freqList[pos][0]:
            if char in ['f', 'i', 'j', 'l', 'r', 't']: # short characters
                adjustLen -= 0.5
            elif char in ['m', 'w']: # long characters
                adjustLen += 0.5
        return (0.9 * adjustLen * findHeight(freqList, pos))/ \
               findHeight(freqList, extreme(freqList,1))
    except IndexError: # error handling for last findWidth()
        return 0 

def displayCloud(freqList):
    """
    Param(s): freqList -> List of tuples (word, frequency in DESC order of frequency
    Sets up a VPython graphics window, displays a Text Cloud
    <http://www.css3.info/preview/hsl/>
    """
    windowSetup()
    maxHeight = findHeight(freqList, 0)
    # Inspiration from <http://bit.do/StackOverflow-ListShuffle>
    random.shuffle(freqList)
    x = -8.5
    y = 5.0
    pos = 0 # number of words added to Text Cloud (current position)
    
    while pos < len(freqList):
        height = findHeight(freqList, pos)
        x_ = (findWidth(freqList, pos) + findWidth(freqList, pos+1))/2 + 0.8
        if x + x_ > 10.5: # next line on Text Cloud
            x = -8.5
            y -= (25 * height)/scene.height
        else:
            myLabel = label(text = freqList[pos][0],
                            pos = (x, y, 0),
                            color = (height/maxHeight, 0.20, 0.45), # HSL format
                            height = height,
                            box = False,
                            border = 0,
                            font = "helvetica")
            x += x_
            pos += 1

def main():
    """
    Function called at program run
    """
    displayCloud(freqList)
    

if __name__=="__main__":
    main()
