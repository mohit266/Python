import requests
import pickle

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(url).text
# print(response)

# split the file into list.
L1 = response.split("\n")
# print(data)

L2 = [item.split(",") for item in L1 if len(item) != 0]
print(L2)

f_write = open("Iris_data.txt", 'wb')
pickle.dump(L2, f_write)
f_write.close()

# Reading the binary data.
file = "Iris_data.txt"
f_read = open(file, 'rb')
data = pickle.load(f_read)
print(data)