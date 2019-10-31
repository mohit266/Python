import json

data = '{"var1":"Mohit", "var2":21}'
# we can use json.load() method to read a file containing JSON object.
parsed = json.loads(data)
print(parsed["var1"])

data2 = {
        "channel_name":"techincal_benders",
        "play_list": ['python', 'c++', 'java', 'Web development'],
        "cars": ('bmw', 'audi'),
        "isbad": False
        }

# we can convert a dictionary to JSON string using json.dumps() method.
jscomp = json.dumps(data2)
print(jscomp)
