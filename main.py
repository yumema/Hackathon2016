#filename: main.py
#purpose: initial testing grounds, new beginnings
#notes: be sure you have file called apiStorage.py
#       in your clone to have api access!

import retinasdk
from apiStorage import apiKey

liteClient = retinasdk.LiteClient(apiKey)
AhriAnalysis = liteClient.getFingerprint("Ahri is a very cute and stupid puppy.")

print(AhriAnalysis)
