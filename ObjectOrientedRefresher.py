# classes are user defined blueprint or prototype
# all operations need to be in class -- a calculator would have sum, mult, add, div, etc inside of the class
# methods, class variables, instance variables, constructor, etc -- terms for classes
# objects for your classes

class Calculator:
    num = 100  # variables created inside a class are class variables

    # init is the keyword to create a consturctor in python
    # The constructor is a method that is called when an object is created of a class
    def __init__(self, a, b):
        self.a = a
        self.b = b # these are called instance variables
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now doing stuff as a method in a class")


object = Calculator()  # This is the syntax to create an object inside of python
object.getData()
print(object.num)
