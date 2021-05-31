import numpy
import json

with open ("spa-eng.dict", "r", encoding='utf-8') as spanish: 
    spatext = spanish.read()

engtext = json.load(open("data.json", "r"))

print(spatext[:140])
print(type(engtext))
