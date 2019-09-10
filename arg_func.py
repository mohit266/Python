# in args function we have to first define normal variable and then args nd then kwargs(optional)
def fun_args(normal, *args, **kwargs):

    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")

if __name__ == '__main__':
    list = ["Mohit", "Navdeep", "Meena", "Jai"]
    normal = "Normal arguement and the students are: "
    kw = {"Mohit":"Programmer", "Navdeep":"Fitness Instructor", "Jai": "Monitor", "Meena":"cook"}
    fun_args(normal, *list, **kw)

