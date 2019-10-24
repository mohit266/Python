# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
#
# print(ls)

# List comprehension
ls = [i for i in range(100) if i % 4 == 0]
print(ls)

# Dictionary comprehension
dict1 = {i: f"Item {i}"for i in range(1, 101) if i % 10 == 0}
print(dict1)

# To change the order of key and value in Dictionary
# - - - Key : value - - - - - - - -
dict2 = {i: f"Item {i}"for i in range(5)}
dict3 = {value: key for key, value in dict2.items()}
print(dict3)

# Set comprehension
set1 = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
print(set1)

# Generator comprehension
gen = (i for i in range(100) if i % 2 == 0)
print(gen.__next__())
print(gen.__next__())