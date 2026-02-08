print("decorators nesting:the output of decorator execution is the input for decorator above")
def stars(func1):
    print("inside 'stars'")
    def inner(text):
        print("inside 'inner' within 'stars'")
        v_input=func1(text)
        return f"***{v_input}***"#"***"+v_input+"***"
    return inner
print("after 'stars'")
def uppercase1(func1):
    print("inside uppercase1")
    def inner(nickname1):
        print("inside 'inner' within 'uppercase1'")
        data = func1(nickname1)
        return data.upper()
    return inner
print("after 'uppercase1'")

@stars#first is written and second to be apply and first be executed
@uppercase1
def getGreeting(nickname):
    return "good morning "+nickname
#getGreeting = stars(uppercase1(getGreeting))
print("after 'getGreeting'")
result = getGreeting("Dangerous Dan")
print(result)
