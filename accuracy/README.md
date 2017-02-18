# Stemming Algorithm

A major part of this project is the algorithm I use to obtain the stems of different words. Stemming is the process of removing inflectional affixes from a word to get the stem, which may not be a valid word.

## Background

While working on this Text Cloud Builder project (as a place-out exam for [Intro to CS](http://eg.bucknell.edu/~csci203/) at Bucknell) during late 2015, I stumbled upon a renowned and one of the most widely used stemming algorithms given by Martin Porter ([here](https://tartarus.org/martin/PorterStemmer/)). I did not want to use someone else's Python code, so I decided to write my own implementation. In the process, however, I realized that Porter's stemmer produced only around 63% valid words.[<sup>[1]</sup>](#fn1) Now you may ask, stems are not necessarily valid words anyway, right? 

Exactly! Thus came the realizaton that I was not actually looking for Porter's stemming algorithm. What I was looking for was an algorithm which gave me valid words which happened to be stems. I thought, such a stemming algorithm would prove to be more beneficial when used for building text clouds or search enginer queries.

## The Challenge

How can the accuracy of the modified stemming algorithm be determined?

  - _Can I compare my output with the output from Porter's stemmer?_ No, because Porter's stemmer does not consider whether the output is a valid word. Then the accuracy of my algorithm would be almost 63%, in which case one should just stick with Porter's algorithm.
  - _Can I check if my output exists in the dictionary?_ Close! But still no, because sometimes the algorithm may stem a word in a way that the output is a valid word but is not the actual stem of the input word.
  
### Potential Solution

To check my output against the closest valid word which is also stemmed, if any stemming is possible at all. As of now, I do not have these reference words, and I need help from volunteers who can _manually_ process all words on Porter's list of input words.[<sup>[1]</sup>](#fn1)

Following are the steps involved:
  - [x] Split the input file into chunks of 500 words each
  - [ ] Process one file at a time
  - [ ] Combine the processed output files
  - [ ] Randomly select 90% of the words and use these words to fine tune the algorithm
  - [ ] Test algorithm on the remaining 10%

### Call for Volunteers

## Notes

<a name="fn1">[1]</a>: Martin Porter published a list of 23531 words [here](https://tartarus.org/martin/PorterStemmer/voc.txt) and their stems [here](https://tartarus.org/martin/PorterStemmer/output.txt).
