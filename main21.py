print("main21")
def tinylog(func):
    def f1(*args, **kwargs):
        args1= [repr(a) for a in args]
        args2= [repr(k)+":"+repr(v) for k, v in kwargs.items()]
        value1= func(*args, **kwargs)
        print("calling", func.__name__, "  ",repr(args1), " ",repr(args2)," ",
              repr(args2), " returns ", value1)
        return value1
    return f1
@tinylog
def total1(a,b):
    return a+b
print(total1(3,4))
print(total1(5,5))
print(total1(8,7))