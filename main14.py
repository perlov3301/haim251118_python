print ("main14.py;callable object as decorator;for class:__init__ + __call__")
class uppercase1:
    def __init__(self, f1, vtext="hello"):
        print(f"inside __init__ ;vtext={vtext}")
        self.f1=f1
        print(f"{self.__class__.__name__} initialized with function: {self.f1.__name__}")
    def __call__(self,vnickname):
        print("inside __call__")
        return self.f1(vnickname).upper()
print("we love coding")

@uppercase1 # class as decorator
def greet(nickname):
    print("inside greet")
    return "good Morning " + nickname
#greet = uppercase1(greet)
print("we love python")
print(greet("dangerous Dan"))