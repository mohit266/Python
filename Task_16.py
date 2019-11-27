vowels = 'aeiou'

ip_str = 'Hello, have you tried facebook new update?'

ip_str = ip_str.lower()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# count the vowels
for char in ip_str:
    if char in count:
       count[char] += 1
print(count)