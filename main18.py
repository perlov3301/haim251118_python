print("main18;")
def bang1(func1):
    print("'bang1' is called")
    def inner():
        print("'inner' of 'bang1'")
        ob=func1()
        return ob
    return inner
print("before decoration for class 'Rectangle'")
@bang1
class Rectangle(): 
    def __init__(self):
        print("init of 'Rectangle'")
        self.x=10
        self.y=20
    def area(self):
        return self.x*self.y
    def __call__(self):
        print("__call of Rectangle")
        return "Hello World from Rectangle"  
print("after decoration for class 'Rectangle'")
ob1= Rectangle()
print("before decoration for class 'Myclass'")
@bang1
class Myclass(): pass
print("after decoration for class 'Myclass'")
ob2= Myclass()
ob3= Rectangle()
def bang2(func2):
    print("'bang2' is called")
    def inner(self):
        print("'inner' of 'bang2'")
        return "this is returned from inner of bang2"
    func2.inner=inner
    return func2
print("before decoration for class 'Myclass2'")
@bang2
class Myclass2(): 
    def method1(self):
        print("method1 of 'Myclass2'")
ob4= Myclass2()
print("before calling ob4.inner()")
print(ob4.inner())
ob4.method1()
def bang3(func1):
    def inner(*tuple1, **dictionary1):
        print("bang3 is called")
        ob=func1(*tuple1, **dictionary1)
        return ob
    return inner
@bang3
class Rectangle1():pass
ob5=Rectangle1()