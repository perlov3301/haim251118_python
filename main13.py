def f_try(v1:int)->bool:
    return True if v1>=0 else False
def f_args(*myargs)->None:
    for index, arg in enumerate(myargs):
        print(f"argument {index}: {arg}")
def f_user_info(username, *mytpl, **mydict):
    print("f_user_info")
    print(f"Username:{username}")
    print(f"details (tuple):{mytpl}")
    print(f"options (dict):{mydict}")
def uppercase(func):
    print("inside uppercase")
    def inner(*args, **kwargs):
        print("inside inner")
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result,str) else result
    return inner

print("we love coding")

@uppercase#get_greeting = uppercase(get_greeting)
def get_greeting(name:str, punctuation:str="!"):
    print("inside get_greeting")
    return f"good morning, {name}{punctuation}"

print("we love python")
v_num=3
v_try=f_try(v_num)
print(f"f_try for {v_num} is {v_try}")
v_tple="apple", "orange", "grape", "lemon"
f_args("apple", "orange", "grape", "lemon")
f_user_info("Alex", "software engineer", "10 years","New York",theme="dark", notifications=True )

print(get_greeting("Alice", punctuation="."))