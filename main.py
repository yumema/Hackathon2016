#filename: main.py
#purpose: initial testing grounds, new beginnings
#notes: be sure you have file called apiStorage.py
#       in your clone to have api access!

from cortLib import *

sampleLite = retinasdk.LiteClient(apiKey)

# creating a filter for domestic pets
domesticPetsFilter = sampleLite.createCategoryFilter(["cat", "puppy", "dog", "kitten", "rabbit", "bunny", "mouse", "rat"])

# determine similarity rating of hamster to the filter
print "hamster has a rate of: " + str( sampleLite.compare(domesticPetsFilter, "hamster") )

# get merged fingerprint of hamster and pets category
newFilter = assimilateTermInCategory( domesticPetsFilter, "hamster")

# determine new similarity rating to updated category
print "hamster has a rate of: " + str( sampleLite.compare(newFilter, "hamster") )
