# collection of unordered items
# mutable and each element is unique
# element is immutable, no indexing is there


from typing import FrozenSet


days = {"Mon", "Tue", "Wed", "Thu"}
set1 = {1,2,"Three",4,5.6}
set2 = {} #that would be empty dict
set3 = set() #that is empty set
days.add("Fri")
days.remove("Mon") #discard() also - in discard, program won't throw error if item isnt there

# s1|s2 = s1.union(s2)
# s1&s2 = s1.intersection(s2)
# s1-s2 = s1.difference(s2)
# s1^s2 = s1.symmetric_difference(s2)

# The frozen sets -  are the immutable form of the normal sets, i.e., the items of the frozen set cannot be changed and therefore it can be used as a key in the dictionary
# frozenset will contain keys of dict

myFrozenset = FrozenSet([1,2,3,4])




