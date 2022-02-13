# A dictionary is used to map or associate things you want to store to keys you need to get them.
# dictionaries do not have order (list have order, dict works on key value pairs)
# need dictionary with order? ==> see 'collections' (orderedDict data structure in pyrhon)

myDict = {'name': 'Brijesh', 'age': 22}
print(myDict)
print(myDict['name'])
myDict['lastname'] = 'Chauhan'
print(myDict)
print("Full Name:", myDict['name']+" "+myDict['lastname'])