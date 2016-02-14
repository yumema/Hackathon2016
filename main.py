#filename: main.py
#purpose: initial testing grounds, new beginnings
#notes: be sure you have file called apiStorage.py
#       in your clone to have api access!

# TODO:
# workflow:
# if prelim definitions don't exist, create definitions
# otherwise, begin analysis of given data
# 
# analysis of data:
#   get fingerprint of new data
#   get similarity coefficient of new data vs known categories
#   append new dataset to category list based on highest coefficient score.
#        catList.append(datasetName)
#   
#   print report of categorized datasets
#   modify existing category fingerprints 


from cortLib import *

categories = "dataset/categories.txt"

def main():
    try:
        categoryFingerprints = open(categories, 'r') #established
    except FileNotFoundError:
        needNewCategories = True        

        catCount = input("Please start establishing categories: ") #write in newcategories
        while needNewCategories:
            establishCategories()
            needNewCategories = addMoreCategories() #continue to add?

        categoryFingerprints = open(oldDefs, 'r')
    
    print(categoryFingerprints)
    catList = getCategories()
    print(catList)
    

if __name__ == "__main__":
    main()
