#       0  ,  1      ,  2       ,   3 --> indexing
l1 = ["AC", "Mobile", "Charger", "Laptop"]
# i =1
# for items in l1:
#     if i%2!=0:
#         print(items)
#     i = i+1
for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"buy {item}")