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
        try:
            self.inPath = argv[1]
            self.inRes = argv[2]
            self.outRes = argv[3]
            self.outPath = argv[4]
        except:
            print("[ERROR] Missing command line argument! See readme for format.")
            quit()

        #declare gen use variables
        self.wFactor = 1
        self.hFactor = 1
        self.workStr = ""

    #this function isolates the width and height of the resolution input argument
    def getResolution(self, getSplit):
        #find x to create substrings 
        i = 0
        for x in getSplit:
            i += 1
            if x == 'x':
                break
        
        #no x, invalid resolution format 
        if i == 0:
            print("[ERROR] Invalid resolution format! See readme for format")
            quit()
        
        #return a touple (width,length)
        resoList = (int(getSplit[:i-1]),int(getSplit[i:]))
        return resoList

    #this function calculates the scale factors for resizing
    def getFactors(self):
        #get inRes, outRes
        splitInRes = self.getResolution(self.inRes)
        splitOutRes = self.getResolution(self.outRes)

        #divide both width and height to find scale factor
        self.wFactor = splitOutRes[0] / splitInRes[0]
        self.hFactor = splitOutRes[1] / splitInRes[1]

        print(self.wFactor)
        print(self.hFactor)
        
        

        

obj = worker(sys.argv)
obj.getFactors()
            
        
