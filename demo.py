#filename: demoObj.py

# A demoObjnstration of how NPL sorts content into categories

from cortClasses import *
from cortLib import *

# categories = "dataset/categories.txt"

def main():

# create categories object
    demoObj = categories()
	
	# start an Issues category based on some terms we'd associate with issues
    demoObj.startNewCategory('Issues', ["problem", "buggy", "bug", "crash", "failed", "help", "broken", "responding", "error", "slow", "died", "BSOD", "restart", "blank", "stuck", "empty", "dead", "breaks"])

    demoObj.startNewCategory('negReviews', ["awful", "bad", "horrible", "disgusting", "poor", "slow", "pricey", "expensive", "boring", "faulty", "inconsistent", "smelly", "stupid"])

    demoObj.startNewCategory('posReviews', ["affordable", "awesome", "good", "great", "nice", "wonderful", "beautiful", "pretty", "fast", "perfect", "efficient", "fantastic", "smart", "clean"])

    print("DEBUGGING SHOW BUCKETS: ")
    demoObj.printBuckets()
	
	# read in files and have them categorized
    with open('dataset/input2.list', 'r') as filelist:
        filename = filelist.readline().replace('\n','')
        while (filename):
            print(filename)
            with open(filename,'r') as file:
                text = file.read()
                file.close()
                findCategory = NLPObject(text, filename)
                demoObj.categorize(findCategory)
            filename = filelist.readline().replace('\n','')

    print("After categorizing: \n")
    demoObj.printBuckets()
	

# run
main()
