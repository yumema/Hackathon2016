#filename: cortClasses.py
#purpose: container for categories class object

from cortLib import *

class categories:
    def __init__(self):
        self.data = {} #key:value, name of category:fingerprint
        self.categoryNames = [] #list of category names contained here
    
    
    def checkCategory(self, candidateCategoryName):
        #TODO: batch function of setting a new category
    
        nameDoesNotExist = True        

        for content in self.categoryNames:
            if newCategoryName == content:
                nameDoesNotExist = False
    
        if nameDoesNotExist:
            self.startNewCategory(candidateCategoryName)
    
    def startNewCategory(self, newCategoryName, 
    
    #input: name - starts a new category with name
    #output: name is appended to list of category names and empty list initialized
    def setCategoryName(self, name):
        self.categoryNames.append(name)
        self.data[name] = []

    #input: name - string: name of category
    #       terms - array of strings: list of defining terms
    #output: new or redefined dict of category name
    def establishFP(self, name, terms):
        newFP = sFunctionFullClient.createCategoryFilter(name, terms)
        self.data[name] = json.dumps(newFP)

    def merge(self, NLPObject):
        #TODO: merge here
        # NLPObjectPositions = NLPObject.positions

    def getFPOf(self, name):
        #TODO: return categoryFP
        return self.data[name]

class NLP_object:
    def __init__(self, text, name = ''):
        self.text = text #handle files too?

        if name == '': 
            self.name = text
        else:   
            self.name = name
    
        self.positions = FunctionLiteClient.getFingerprint(self.text)
        self.keywords = FunctionLiteClient.getKeywords(self.text)

    def showName(self):
        print(self.name)
    def showText(self):
        print(self.text)
    def showFP(self):
        print(self.positions)
    def showKW(self):
        print(self.keywords)

    def getName(self):
        return self.name
    def getText(self):
        return self.text
    def getFP(self):
        return self.positions
    def getKeywords(self):
        return self.keywords

    def compareToCategories(self, categories):
        #TODO: compare to category here
        # return sim coeff
    def compareToCategory(self, categoryFP, categoryName):
        #TODO: compare to single category, return similarity coeff
        return FunctionLiteClient.compare(self.positions, categoryFP.getFPOf(categoryName)
    def compareToOther(self, other):
        return FunctionLiteClient.compare(self.positions, other)
    def 
