# this will inherit all parent properties for your test cases
# first class is usually for invoking brower function -- you can call that immediately in child

# you must import the class from previous file
from ObjectOrientedRefresher import Calculator

# pass in parent to child class to get all of its data
class ChildClass(Calculator):
    num2 = 200

    def getCompleteData(self):
        # if you want to use anything inside of a class, it needs to start with self. or className.
        # we can now access data from the parent class
        return self.num2 + self.num

obj = ChildClass()

