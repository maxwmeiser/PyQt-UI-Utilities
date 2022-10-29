from asyncio.windows_events import NULL
from asyncore import write
import sys, re, string


#   command line args
#   1) input UI file path
#   2) output UI file path
#

class worker():
    def __init__(self, argv):
        
        #declare command line arguments 
        try:
            self.inPath = argv[1]
            self.outPath = argv[2]
        except:
            print("[ERROR] Missing command line argument! See readme for format.")
            quit()

        #two cases of lines to be modified 
        self.regexPressionNormal = "\s*((<pixmap>)|(<normaloff>)|(<normalon>)|(<disabledoff>)|(<disabledon>)).*((<\/pixmap>)|(<\/normaloff>)|(<\/normalon>)|(<\/disabledoff>)|(<\/disabledon>))"
        self.regexPressionEndiconset = "\s*.*(<\/iconset>)"

    def readWrite(self):
        #opens two files, readFile and writeFile
        readFile = open(self.inPath, 'r')
        writeFile = open(self.outPath, 'w')

        #get lines from readFile. Returns a list with all lines within the file
        readLines = readFile.readlines()
        """
        iterate through lines
            Check every line with both regex expressions to see if line of interest
                If match on endIconset
                    modify both filepaths in line
                    write to outfile
                else if match on Normal
                    modify the filepath in line
                    write to outfile
                else
                    write to outfile      
        """
        for line in readLines:
            normalMatch = re.search(self.regexPressionNormal, line)
            iconsetMatch = re.search(self.regexPressionEndiconset, line)
            if iconsetMatch != None:
                writeFile.write(self.modLine(1,line))
            elif normalMatch != None:
                writeFile.write(self.modLine(0,line))
            else:
                writeFile.write(line)

    def modLine(self, type, line):
        if type == 0:
            #normal match, replace 1 url
            startIndex = 0
            endIndex = 0
            count = 0
            
            #iterate over line char by char, find position of first '>' and second '<'
            for char in line:
                if char == '>' and startIndex == 0:
                   startIndex = count
                elif char == '<' and startIndex > 0:
                    endIndex = count
                count += 1
            
            #create and modify substring based of indexes 
            substr = line[startIndex+1:endIndex]
            modSubstr = "../" + substr

            return line.replace(substr, modSubstr)

        else:
            #iconset match, replace 2 urls
            greaterOneIndex = 0
            greaterTwoIndex = 0
            lessOneIndex = 0
            lessTwoIndex = 0
            count = 0

            #iterate over line, set indexes of first, second > and <
            for char in line:
                if char == '>':
                    if greaterOneIndex == 0:
                        greaterOneIndex = count
                    else:
                        greaterTwoIndex = count
                if char == '<':
                    if greaterOneIndex != 0 and lessOneIndex == 0:
                        #if past first > and first < encountered
                        lessOneIndex = count
                    elif lessOneIndex != 0:
                        #break loop, last relevant index position needed
                        lessTwoIndex = count
                        break
                count += 1
            
            print("g1I: " + str(greaterOneIndex) + " | l1I: " + str(lessOneIndex) + " | g2I: " + str(greaterTwoIndex) + " | l2I: " + str(lessTwoIndex))
            #create two substrings, modify them, and replace original substrings with modded
            ss1 = line[greaterOneIndex+1:lessOneIndex]
            ss2 = line[greaterTwoIndex+1:lessTwoIndex]

            #edge case where file path is the same
            if ss1 == ss2: 
                mod1 = "../" + ss1
                line = line.replace(ss1, mod1)
            else: 
                mod1 = "../" + ss1
                mod2 = "../" + ss2
                line = line.replace(ss1, mod1)
                line = line.replace(ss2, mod2)
            
            return line


    def primary(self):
        self.readWrite()

        

obj = worker(sys.argv)
obj.primary()

            
        
