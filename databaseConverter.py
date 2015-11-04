__author__ = 'Toasty'
import urllib2
import os

completeName = os.path.abspath("C:/Users/Toasty/Desktop/newTicTac.txt")#new file destination
newFile = open(completeName, "w")
url = urllib2.urlopen("http://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data") #url of .data file
data = url.read()
data2 = data.split("\n")
for line in data2:
    vals = line.split(",")
    classifier = vals[len(vals) - 1] #for classifiers as last line value
    if classifier == "positive": #original classifier 1
        classifier = "[1,0]"
    elif classifier == "negative": #original classifier 2
        classifier = "[0,1]"
    vals[len(vals) - 1] = classifier
    for item in vals[:-1]:
            newFile.write("%s," % item)
    newFile.write(vals[len(vals) - 1])
    newFile.write("\n")
