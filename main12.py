def uppercase1(func):
    print("inside uppercase")
    def inner():
        print("inside inner")#uppercase1 returns inner
        data = func() 
        return data.upper()#method of python
    return inner#prints "inside inner"

print("we love coding!")#printed first

@uppercase1 #prints "inside uppercase"
def getGreeting():
    print("inside getGreeting")
    return "good morning"
#equivalent:getGreeting = uppercase1(getGreeting)

print("we love python!")
print(getGreeting())