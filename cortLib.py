import json
import retinasdk
from apiStorage import apiKey

# helper functions

# reusable client for handling API calls
sFunctionFullClient = retinasdk.FullClient(apiKey,
                apiServer="http://api.cortical.io/rest",
                retinaName="en_synonymous")

aFunctionFullClient = retinasdk.FullClient(apiKey,
                apiServer="http://api.cortical.io/rest",
                retinaName="en_associative")

# input: category - a fingerprint of the category filter
#        term     - the term you want to add to the category
# output: the resulting fingerprint of assimilating given term
def assimilateTermInCategory(category, term):
	orExpression = {"or": [{"positions": category}, {"term": term}]}
	return sFunctionFullClient.getFingerprintForExpression(json.dumps(orExpression)).positions

#input: FP1 - fingerprint 1 to be merged with FP2
#       FP2 - fingerprint 2
# output: the resulting fingerprint of merging FP1 and FP2
def mergeFingerprints(FP1, FP2):
	orExpression = {"or": [{"positions": FP1}, {"positions": FP2}]}
	return sFunctionFullClient.getFingerprintForExpression(json.dumps(orExpression)).positions

# input: category - a fingerprint of the category filter
#        term     - the term to be disassociated with the category
# output: the resulting fingerprint of removing a term's association with the given category
def removeTermFromCategory(category, term):
	subExpression = {"sub": [{"positions": category}, {"term": term}]}
	return sFunctionFullClient.getFingerprintForExpression(json.dumps(subExpression)).positions

#input: FP1 - fingerprint 1 to be merged with FP2
#       FP2 - fingerprint 2
# output: the resulting fingerprint of removing FP2 from FP1
def disassociateFingerprints(FP1, FP2):
	subExpression = {"sub": [{"positions": FP1}, {"positions": FP2}]}
	return sFunctionFullClient.getFingerprintForExpression(json.dumps(subExpression)).positions

def exEstablishCategories():
    infile = open('dataset/categories.txt', 'w+')
    
    #dummy categories
    dogs = 'dog breeds'
    dogsList = ['pomeranian', 'papillion', 'daschund', 'corgi']
    dogFingerprint = sFunctionFullClient.createCategoryFilter(dogs, dogsList)
    json.dump(dogFingerprint.__dict__, infile)

    infile.write('\n')

    cars = 'cars'
    carsList = ['BMW', 'Ford', 'Toyota']
    carsFingerprint = sFunctionFullClient.createCategoryFilter(cars, carsList)
    json.dump(carsFingerprint.__dict__, infile)
       
    infile.close()

#input: user provides category name and criteria
#output: write to categories file
def establishCategories():
    outfile = open('dataset/categories.txt', 'w')
    
    newCat = input('New category name: ')
    newFilters = []
    
    for i in range(0, 3):
        newFilters.append(input('Provide Filter: '))

    outfile.write('\n') # separate lines out    

    outfile.close()

#input: nothing
#output: return list of established categories from file
def getCategories():
    catList = []    

    with open('dataset/categories.txt', 'r') as infile:
        for line in infile:
            catList.append(json.loads(line))

    print(catList[0]['categoryName'])
    
    infile.close()
    
    return catList

