#!/bin/bash
# Script to stem all words of a text file

# creates output directory if does not exist already
mkdir -p output

# generates name of output file using current time
dt=$(date '+%d_%m_%Y_%H_%M_%S')
ext="txt"
filename="output_$dt.$ext'"

# saves output of accuracy tester script to file
python accuracy.py > output/"$filename'"