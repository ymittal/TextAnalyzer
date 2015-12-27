from visual import *

def windowSetup():   
    """" Sets up the VPython window "scene"
         See http://www.vpython.org/webdoc/visual/display.html"""
    
    scene.autoscale = false        # Don't auto rescale
    scene.background = color.white
    scene.foreground = color.black
    scene.height = 1000            # height of graphic window in pixels
    scene.width = 1000             # width of graphic window in pixels
    scene.x = 100                  # x offset of upper left corner in pixels
    scene.y = 100                  # y offset of upper left corner in pixels
    scene.title = 'Text Cloud'

def createSortedList():
    """ createSortedList returns a list of tuples containing a common word
        and its count for testing displayCloud().  The list is sorted on the
        counts from highest to lowest.  Returns a similar data structure as
        expected from text cloud analyzer. """
    
    # 31 most common words on CSCI 203 home web page, values are random
    sortedList = [('lab', 19), ('homework', 16), ('due', 13), ('monday', 12),
                  ('dana', 9), ('prof', 7), ('academic', 6), ('course', 5),
                  ('exam', 5), ('instructor', 5), ('oct', 4), ('nov', 4),
                  ('university', 4), ('sept', 4), ('submit', 4), ('work', 4),
                  ('guide', 4), ('student', 4), ('mwf', 3), ('policy', 3),
                  ('resource', 3), ('lecture', 3), ('understand', 3),
                  ('problem', 3), ('read', 3), ('principle', 3), ('python', 2),
                  ('practice', 2),  ('dishonest', 2),
                  ('specific', 2), ('computer', 2)]
    return sortedList

def displayCloud(sortedList):
    """ Displays on a VPython graphics window the text cloud
        Input: sortedList - a list of tuples with first item a common word
               and second item the count for that word.  Sorted from high
               to low on counts. """
    
    y = 10          # scene coordinates at top is 10
    maxHeight = 100 # max height of letter in pixels
    
    maxCount = sortedList[0][1]
    myLabels = []
    for w in range(len(sortedList)):

        # wordHeight is proportional to word's count
        wordHeight = sortedList[w][1]/maxCount * maxHeight

        # add another label object to list
        # See http://www.vpython.org/webdoc/visual/label.html
        myLabels += [ label(text = sortedList[w][0], pos = (0, y, 0),
                    color = (1 - wordHeight/maxHeight, 0, wordHeight/maxHeight),
                    height = wordHeight, box = 0, border = 0, font = "times") ]
        
        y = y - 25/scene.height * wordHeight # move down y for next word

    # How to access one of the labels in the list of label objects
    # and change an attribute's value
    # Uncomment the next line to change the first word to green.
    # myLabels[0].color = (0, 1, 0)
    
def main():
    windowSetup()
    displayCloud(createSortedList())
