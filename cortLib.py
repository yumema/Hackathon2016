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
# output: the new fingerprint 
def assimilateTermInCategory(category, term):
	orExpression = {"or": [{"positions": category}, {"term": term}]}
	return sFunctionFullClient.getFingerprintForExpression(json.dumps(orExpression)).positions
