#filename: cortClasses.py
#purpose: container for categories class object

from cortLib import *

class categories:
    def __init__(self):
        self.data = {} #key:value, name of category:fingerprint
        self.names = [] #list of category names contained here
        self.bucket = {} #list of NLPObject names that have been categorized
    #input: candidateCategoryName - string: potential new name of category
    #output: if given designation does not exist, start creating new category
    def checkCategory(self, candidateCategoryName):
        nameDoesNotExist = True        

        for content in self.categoryNames:
            if newCategoryName == content:
                nameDoesNotExist = False
    
        if nameDoesNotExist:
            self.startNewCategory(candidateCategoryName)
    
    #input: newCategoryName - string: name of new category
    #output: starts creating new categories and fingerprints
    def startNewCategory(self, newCategoryName, termsList=[]):
        self.setCategoryName(newCategoryName)
        self.establishFP(newCategoryName, termsList)
        self.startBucket(newCategoryName)   
 
    #input: name - starts a new category with name
    #output: name is appended to list of category names and empty list initialized
    def setCategoryName(self, name):
        self.names.append(name)
        self.data[name] = []

    #input: name - string: name of category
    #       terms - array of strings: list of defining terms
    #output: new or redefined dict of category name
    def establishFP(self, name, terms):
        newFP = sFunctionFullClient.createCategoryFilter(name, terms).positions
	#self.data[name] = json.dumps(newFP)
	self.data[name] = newFP

    #in:    name - name of new bucket
    #out:   new bucket list created
    def startBucket(self, name):
        self.bucket[name] = []

    #in:    name - name of bucket to be added to
    #       NLPObjectName - NLPObject to be added
    #out:   modified bucket
    def addToBucket(self, name, NLPObject):
        self.bucket[name].append(NLPObject.getName())

    #in:    name - name of category
    #       NLPObject - object to be categorized
    #out: calls to addToBucket and merge
    def categorize(self, NLPObject):
	name = self.determineBucket(NLPObject)
	print "DEBUG: categorize decided on " + str(name)
        self.addToBucket(name, NLPObject)
        self.merge(name, NLPObject)

    #in:  NLPObject - the NLPObject we want categorized
    #out: returns name of category NLPObject best fits 
    def determineBucket(self, NLPObject):
        categoryName = ""
        bestRate = 0
        for name in self.names:
            simValue = FunctionLiteClient.compare(self.data[name], NLPObject.getFP())
            if (simValue > bestRate):
                bestRate = simValue
                categoryName = name 
        return categoryName

    #in:  name - name of category to be modified
    #     NLPObject - NLPObject to be used to incorporated into category
    #out: category fingerprint is modified
    def merge(self, name, NLPObject):
        orExpression = {"or": [{"positions": self.data[name]}, {"positions": NLPObject.getFP()}]}
        self.data[name] = sFunctionFullClient.getFingerprintForExpression(json.dumps(orExpression)).positions

    #getters
    def getFPOf(self, name):
        return self.data[name]

    #show-ers
    def printBuckets(self):
	print self.bucket

class NLPObject:
    def __init__(self, text, name =''):
        self.text = text #handle files too?

        if name == '': 
            self.name = text
        else:   
            self.name = name
    
        self.positions = FunctionLiteClient.getFingerprint(self.text)
        self.keywords = FunctionLiteClient.getKeywords(self.text)

    #show-ers
    def showName(self):
        print(self.name)
    def showText(self):
        print(self.text)
    def showFP(self):
        print(self.positions)
    def showKW(self):
        print(self.keywords)

    #getters
    def getName(self):
        return self.name
    def getText(self):
        return self.text
    def getFP(self):
        return self.positions
    def getKeywords(self):
        return self.keywords

    #in - categories object
    #out - dict with keys as catNames and values as simCoeff
    def compareToCategories(self, categories):
        comparisonData = {}
        for catName in categories.names:
            comparisonData[name] = FunctionLiteClient.compare(self.positions, categories.getFPOf(name))
        return comparisonData
        
    #in - categories object
    #out - returns tuple of the name of the category and the simCoeff
    def getBestMatch(self, categories):
        categoryName = ""
        bestRate = 0
        for name in categories.names:
            simValue = FunctionLiteClient.compare(self.positions, categories.getFPOf(name))
            if (simValue > bestRate):
                bestRate = simValue
                categoryName = name 
        return(categoryName, bestRate)

    def compareToCategory(self, categoryFP, categoryName):
        return FunctionLiteClient.compare(self.positions, categoryFP.getFPOf(categoryName))
    def compareToOther(self, other):
        return FunctionLiteClient.compare(self.positions, other) 
