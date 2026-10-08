class Person:
    def __init__(self, name, middle_name, last_name, age):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age


    def get_info(self):
        print(f"Name: {self.name}\n"
              f"Middle name: {self.middle_name}\n"
              f"Last name: {self.last_name}\n"
              f"Age: {self.age}\n")
        return


class Parent(Person):
    def __init__(self, name, middle_name, last_name, role="Spouse", age=None):
        super().__init__(name, middle_name, last_name, age)
        self.role = role
        self.children = []


    def add_child(self, child):
        child_name = child.name
        self.children.append(child_name)


    def get_status(self):
        print(f"Status: {self.role}\n"
              f"Children: {self.children}\n")


class Child(Person):
    def __init__(self, name, father):
        self.father = father
        last_name = father.last_name
        middle_name = father.name
        self.role = "Child"
        super().__init__(name, middle_name, last_name, age=0)


class Family:
    def __init__(self, member, *args):
        self.name = member.last_name
        self.members = {x.name: x.role for x in args}

    def get_composition(self):
        print(f"Сomposition of {self.name}: {self.members}\n")


class City:
    def __init__(self, name, *args):
        self.name = name
        self.families = [x.name for x in args]


    def get_families(self):
        print(f"Families in {self.name}: {self.families}\n")


John = Parent("John", "Kelly", "Smith", "Father", 35)
Caroline = Parent("Caroline", "Ray", "Smith", "Mother", 29)
John.get_info()

Michael = Child("Michael", John)
Erica = Child("Erica", John)
Michael.get_info()

John.add_child(Michael)
John.add_child(Erica)
John.get_status()

Smith = Family(John, Caroline, Michael, Erica)
Smith.get_composition()

Henry = Parent("Henry", "Sam", "Brown", "Spouse", 56)
Alice = Parent("Alice", "Peter", "Brown", "Spouse", 45)
Alice.get_info()

Brown = Family(Henry, Alice)

San_Francisco = City("San Francisco", Smith, Brown)
San_Francisco.get_families()

