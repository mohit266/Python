s1 = input("Enter first string")
s2 = input("Enter second string")

if sorted(s1) == sorted(s2):
    print("The strings are anagram")

else:
    print("String aren't anagram")
