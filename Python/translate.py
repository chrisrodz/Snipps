# Python module for translating .srt files from english to spanish
# Christian A. Rodriguez January 24th, 2013
# Usage: python translate.py spanish.txt english.srt newfile.srt
#
# spanish.txt = The text in the .srt translated to spanish
# english.srt = The .srt file to be translated
# newfile.srt = The name of the new .srt file to be created
#
# The program will take each line from spanish.txt and create newfile.srt
# replacing the appropiate lines with the translated text

import sys

if len(sys.argv) != 4:
	print "Usage: python translate.py spanish.txt english.srt newfile.srt"
	sys.exit()

# Get the spanish lines from spanish.txt

spanish = open(sys.argv[1])
translated_lines = []
for line in spanish:
	translated_lines.append(line)
spanish.close()
translated_lines.reverse()

# Get all of the lines from the original .srt file
srt = open(sys.argv[2], 'r')
english = srt.readlines()
srt.close()

# Replace the text lines with the translated text
newlines = []
i = 0
while len(translated_lines)>0:
	for j in range(0,3):
		newlines.append(english[i+j])
	newlines.append(translated_lines.pop())
	i += 4

# Create the new .srt file with the translated text
newfile = open(sys.argv[3],'w')
for line in newlines:
	newfile.write(line)
newfile.close()
