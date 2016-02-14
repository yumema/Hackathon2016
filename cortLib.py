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
	return sFunctionFullClient.getFingerprintForExpression(json.dumps(orExpression)).positions
