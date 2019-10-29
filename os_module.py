# The OS module in python provides functions for interacting with the operating system.
import os

# To get current working directory
print(os.getcwd())

# To make directory
os.mkdir("yo")

# To remove directory
os.rmdir("yo")

# To make directories
os.makedirs("Tutorials/Python")

# To check path is exist or not
print(os.path.exists("/home/mohit/Desktop/Python-program"))

