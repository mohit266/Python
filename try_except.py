try:
    f = open("file.txt")

# We can Write multiple Exception statements
except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    f.close()
