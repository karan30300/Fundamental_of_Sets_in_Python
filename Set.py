"""
Set:
is Mutable 
is a collection of unorderd items
each element in set is Must be Unique & Immutable(Not changable)
we can add Boolean, int, Float, String, Tuple Data type in Set (Store Immutable Data Type)
But, Not Store list add Dict because "list, Dict" are Mutable
"""

collection = { 1,2,2,4,'jhon', 'Hello'}#Ignore Duplicate Values and Store Single Unique Values
print(collection)
print(type(collection))
print(len(collection)) #Give Total No. of unique Elements/Items (Ignore Duplicates In Counting)


# Note: If we want to cretae a Empty Set Must use "set()" function Not collection = {} == Data type is Dictionary not Set
s1 = {} # Create A Empty Dictionary
s2 = set() # Cretae a Empty Set
print(type(s1))
print(type(s2))


# "Stes are "Mutable" means we can add or remove Elements In exsisting Set., But sets Elemets are "Immutable" 

"""
Sets Methods:
set.add(elm) = add an element [we can not add list and Dict only add tuple in ".add()" method]
set.remove(elm) = remove the element
set.clear() = Empty set
set.pop() = Remove a rendom value
set.union(set2) = combine both set value and give new 
set.intersection(set2) = give comman value of Both sets and give new value
"""
data = set() #empty set

#.add()
data.add('karan') #add a single Element
data.add((10,20,30)) #add Tuple in Set
data.add(50)
data.add(20)
data.add(50)
data.add(True)
print(type(data),data)
print(len(data))

#.remove()
print(f"Before Remove Element :{data}")
data.remove('karan') #remove "karan" from set
print(f"After Remove Element :{data}")

#.pop()
print(data)
data.pop() #pop() remove a Random Element from Set
print(data)

#.clear()
print(f"Length of Set Before: {len(data)}")
print(data.clear()) #Clear all Values/Elements from set
print(f"Length of Set After: {len(data)}")

# set.union()
a = {10,20,50,40,True,'Karan'}
b = {10,50,False}

c = a.union(b) #combine both set and maek a one new set with all values 
print(f"Common value of Both Sets: {c}")

# set.intersection()
d = {10,20,50,40,True,'Karan'}
e = {10,50,False}

f = d.intersection(e) #combine both sets value and give only Comman Values

print(f)