import os


def soldier(inp_path, format):
    ls = []
    # It checks whether the entered path is valid or not.
    if os.path.exists(inp_path):
        os.chdir(inp_path)
        print("Entered path is valid")

        # It returns the list of directories or files on the given path.
        files = os.listdir(inp_path)

        # It capitalize the first letter of file and directory present in given path.
        for i in files:
            ls.append(i)
            os.rename(i, i.capitalize())
        print(ls)

        i = 1

        # It rename the files of same format.
        for file in files:
            if os.path.splitext(file)[1] == format:
                os.rename(file, f'{i}{format}')
                i += 1
    else:
        print("Please Try again !!! Your entered path is invalid")

if __name__ == '__main__':

    inp_path = input("Enter valid path :")
    format = input("Enter extension of file or image : ")
    soldier(inp_path, format)
