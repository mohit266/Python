import time


def name_searcher():
    f = open("names.txt")

    while True:
            read_file = (yield)
            if read_file in f.read():
                print("Your name is in the file")
            else:
                print("Your name is not in the file")

if __name__ == '__main__':
    read_file = input("Enter your name:")
    search = name_searcher()
    print("Searching...")
    time.sleep(2)
    next(search)
    search.send(read_file)
