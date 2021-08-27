# Numbers
print("Numbers")
print("-----------------")
num = 50 + 50
print(num)

# Powers
num = 2**3
print('2 ^ 3 = ' + str(num))

# String
print("\nStrings")
print("-----------------")

st = "hello world"
print("Hello World: 10")
print(st[0])

# [start:stop:step]
print(st[0:7:2])

# List
print("\nLists")
print("-----------------")

l = [0,1,3,"f"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:5])
print(thislist[-4:-1])

thislist[1] = "blackcurrant"
thislist[3:5] = ["blackcurrant"]
thislist.append("orange")
thislist.insert(2, "watermelon")
thislist.remove("apple")

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 8, 5
Matrix = [[0 for x in range(w)] for y in range(h)] 

# Dictionaries
print("\nDictionaries")
print("-----------------")
dict = {'key': 'value'}
print(dict)

# Tuples
print("\nTuples")
print("-----------------")
tup = (1,3,5)
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)