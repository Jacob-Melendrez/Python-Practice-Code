class Parent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Parent speaking")


class Child(Parent):  # inherits from Parent
    def __init__(self, name, age):
        super().__init__(name)  # call Parent constructor
        self.age = age

    def speak(self):  # override method
        print("Child speaking")


# usage
c = Child("Alex", 10)
c.speak()        # overridden method
print(c.name)    # inherited attribute