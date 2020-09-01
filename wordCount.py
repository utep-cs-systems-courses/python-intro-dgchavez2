#! /usr/bin/ python3

import sys
import re
import os
import subprocess

inputFname = sys.argv[1]
outputFname = sys.argv[2]

def main():
    #reading file
    file = open(inputFname, "r")
    document = file.read()
    file.close()
    #ignoring case
    document = document.lower()
    #calls func and sorts the returned list, initializing dictionary
    # to get ready for output file
    word_list = get_words(document)
    word_list = sorted(word_list)
    dic = {}

    #counts words
    for word in word_list:
        if word not in dic:
                dic[word] = 1
        else:
            dic[word] += 1

    file = open(outputFname, "w")

    for word in dic:
        file.write(word + " " + str(dic.get(word)) + "\n")

    file.close()

#func that returns list of words with no special chars
def get_words(document):
    word_list = []

    #regex substitutes all non words or underscores with a space
    #since \W doesn't include _ i had to include or statement
    document = re.sub("\W+", " ", document)
    #for word in document:
     #   print(word)
      #  word_list.append(word)
    word_list = document.split()
    return word_list

main()