#filename: cortClasses.py
#purpose: container for categories class object

from cortLib import *

class categories:
    def __init__(self):
        self.data = {} #key:value, name of category:fingerprint
        self.names = [] #list of category names contained here
    
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
    def startNewCategory(self, newCategoryName):
        self.setCategoryName(newCategoryName)
        self.establishFP(newCategoryName, termsList)
    
    #input: name - starts a new category with name
    #output: name is appended to list of category names and empty list initialized
    def setCategoryName(self, name):
        self.names.append(name)
        self.data[name] = []

    #input: name - string: name of category
    #       terms - array of strings: list of defining terms
    #output: new or redefined dict of category name
    def establishFP(self, name, terms):
        newFP = sFunctionFullClient.createCategoryFilter(name, terms)
        self.data[name] = json.dumps(newFP)

    #in:  name - name of category to be modified
    #     NLPObject - NLPObject to be used to incorporated into category
    #out: category fingerprint is modified
    def merge(self, name, NLPObject):
        orExpression = {"or": [{"positions": self.data[name]}, {"positions": NLPObject.getFP()}]}
        self.data[name] = sFunctionFullClient.getFingerprintForExpression(json.dumps(orExpression)).positions

    #getters
    def getFPOf(self, name):
        return self.data[name]

class NLPObject:
    def __init__(self, text, name = ''):
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
