import sys

#   command line args
#   1) input UI file path
#   2) input file resolution in the form <WIDTH>x<HEIGHT>
#   3) output file desired resolution in the form <WIDTH>x<HEIGHT>
#   4) output UI file path
#

class worker():
    def __init__(self, argv):
        
        #declare command line arguments 
        self.inPath = argv[1]
        self.inRes = argv[2]
        self.outRes = argv[3]
        self.outPath = argv[4]

        #declare gen use variables
        self.wFactor = 1
        self.hFactor = 1
        self.workStr = ""
        
