print("main19; decorator with arguments")
def bang1(text:str, repeat1:int=1):
    print("bang1")
    def f1(func):
        print("f1")
        def inner():#will be called when we create object of class
            print("inner")
            print((" "+text)*repeat1 if repeat1>1 else text)
            ob=func()
            return ob
        return inner
    return f1
@bang1(text="hello", repeat1=3)
class Rectangle1(): pass
ob1=Rectangle1()

def bang2(text, repeat1=1):
  def f1(func):
    def inner(*tpl, **dctnr):
       print((" "+text)*repeat1 if repeat1>1 else text)
       return func(*tpl, **dctnr)
    return inner
  return f1
@bang2(text="Constructing Rectangle2")
class Rectangle2:
   def __init__(self, width, height=1, **kwargs):
      self.width=width
      self.height=height
      self.extra=kwargs
   def area(self):
      return self.width*self.height
rect1= Rectangle2(3,height=4, color="red")
print(f"area of rectangle is {rect1.area()}")
print(f"rectangle's color is {rect1.extra.get('color')}")
print(f"rectangle's area is {rect1.extra.get('area')}")
