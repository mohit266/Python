# Adjacent element.

a = input("Enter any string:")
new = " "
counter = 0
for i in a.lower():
    if new[counter]!=i:
        new += i
        counter += 1

print(new)