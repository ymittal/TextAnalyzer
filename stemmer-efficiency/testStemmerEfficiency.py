from stemmer import ModifiedStemmer

toBeStemmed, originalStemmed = [], []

with open("voc.txt") as fin:
    toBeStemmed = fin.read().splitlines()
    
with open("output.txt") as fin:
    originalStemmed = fin.read().splitlines()
    
s = ModifiedStemmer()
count = 0

for i in range(len(toBeStemmed)):
    word = toBeStemmed[i]
    if len(word) > 1:
        toBeStemmed[i] = s.stem(word)
        if toBeStemmed[i] == originalStemmed[i]:
            count += 1

print ("Efficiency: ", (count/len(originalStemmed))*100, "%")
            
    
    
