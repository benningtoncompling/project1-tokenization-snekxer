"""
Write a program that can clean a file and count the words in it. It should run using the
following command in the terminal:

./clean_and_count_tokens.py <input_file> <output_file>

The input file to clean is in xml, which contain tags encased in <>. These tags should
not be counted. All other words are counted.
"""
#This means everything else, including URLs and assorted oddities, should be skimmed for words
"""
A word may only contain the following:
- Capital letters
- Lowercase letters
- the straight apostrophe '
- internal periods (with alphabetic characters on either side)

Words should count towards the tally regardless of capitalization. Ex: 'Is' and 'is'
should both count as instances of 'is'

Write the results to a file, one word per line with the count IN ORDER from most
common to least common. Ties should be in alphabetical order. There should be a
single tab between the word and the count.

A sample input/output is included in the folder. Please take a look!

Please run your code on the included Wikipedia-LexicalAnalysis.xml, and call the
output file lexical_analysis_out.txt

You may only import: sys, re (or regex)

Your submission should include the following 2 files:
1. clean_and_count_tokens.py
2. lexical_analysis_out.txt

Depending on how you organize your code, you may have more files than this.
"""

import sys
import regex

file = open("Wikipedia-LexicalAnalysis.xml", "r", encoding="utf-8").read()
print(file)

#remove XML tags
file = regex.sub(r"<.+?>|\&lt\;.+?\&gt\;", "", file, flag="UNICODE")
file = file.casefold()
newfile = open("lexical_analysis_out.txt", "w+",  encoding="utf-8").write(file)

#gets words (after cleanup)
file = regex.findall(r"\b(?:[a-zA-Z]+[\.\']?[a-zA-Z]?)+\b", file, flag="UNICODE")

file.sort()

print(file)
#newfile = open("lexical_analysis_out.txt", "w+",  encoding="utf-8").write(file)