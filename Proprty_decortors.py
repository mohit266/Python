class Student:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def print_detail(self):
        return f"Name of student is {self.f_name} {self.l_name}"

    @property
    def email(self):
        if self.f_name == None or self.l_name == None:
            return "Email is not set. Please set it using setter"
        return f"{self.f_name}.{self.l_name}@gmail.com "

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        # print(names)
        self.f_name = names.split(".")[0]
        self.l_name = names.split(".")[1]

    @email.deleter
    def email(self):
        self.f_name = None
        self.l_name = None

st = Student("Mohit", "Suthar")

print(st.email)

st.f_name = "Rahul"
print(st.email)

st.email = "ms.dhoni@gmail.com"
print(st.email)

del st.email
print(st.email)