print("main15; callable class as decorator; *args1, **kwargs1")
class uppercase2:
    def __init__(self, f1, vtext="hello"):
        print(f"inside __init__;vtext={vtext}")
        self.f1=f1
        print(f"{self.__class__.__name__} initialized with function: {self.f1.__name__}")
    def __call__(self, *tuple1, **dictionary1):
            print("inside __call__")
            return self.f1(*tuple1, **dictionary1).upper()
print("we love coding")

@uppercase2
def greet(nickname):
    return "good Morning"+ " " + nickname
#greet = uppercase2(greet)

print("we love python")
print(greet(nickname="dangerous Dan"))
def f_args(v1, *tuple1, **dictionary1):
  print(f"required: {v1}")
  print(f"optional tuple: {tuple1}")
  print(f"optional dict: {dictionary1}")
f_args("string value", 1,2,3, key1="value1", key2= 2)