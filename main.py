#filename: main.py
#purpose: initial testing grounds, new beginnings
#notes: be sure you have file called apiStorage.py

# TODO: workflow
# simulate construction of categories from scratch
# create - 
# provide a text file with information relevant to one of those categories
# compare fingerprint from text file to fingerprints of categories
# determine bestMatch (highest simCoefficient).

from cortClasses import *
from cortLib import *

categories = "dataset/categories.txt"

def main():
    """ ideal case: establish new if necessary
    try:
        categoryFingerprints = open(categories, 'r') #established
    except FileNotFoundError:
        needNewCategories = True
        catCount = input("Please start establishing categories: ") #write in newcategories
        while needNewCategories:
            establishCategories()
            needNewCategories = addMoreCategories() #continue to add?
    """
    #exEstablishCategories()

#test case: fileToFingerprint

    #fileFingerprint = (fileToFingerprint('dataset/cv001_18431.txt'))
    
    textAnalysis = NLP_object('Apple computers keep crashing', 'bug report #003')
    textAnalysis.showName()
    print(textAnalysis.compareToOther('Macintosh is the best!'))

#test case: compare
    #compareCategoryList = getCategories()
    #compareValue = input("provide string: ")
    #print(compare(compareCategoryList[0]['positions'], fileFingerprint))

if __name__ == "__main__":
    main()
