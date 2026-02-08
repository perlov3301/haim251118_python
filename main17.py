print("main17;decorators nesting with parameters")
def stars(func1):
  print("inside 'stars'")
  def inner(*tuple1, **dictionery1):
    print("inside 'inner' within 'stars'")
    v_output=func1(*tuple1, **dictionery1)
    return f"***{v_output}***" if isinstance(v_output,str) else v_output
  return inner
print("after 'stars'")

def uppercase1(func2):
  print("inside uppercase1")
  def inner(*tuple1, **dictionery1):
    print("inside 'inner' whithin uppercase1'")
    result=func2(*tuple1, **dictionery1)
    return result.upper() if isinstance(result, str) else result
  return inner
print ("after 'uppercase1'")

@stars #entering 'stars'  after uppercase1
@uppercase1 #entering 'uppercase1'  first
def greet(name, punctuation1="."):
  print("inside 'greet'")
  return f"Good Morning {name}{punctuation1}"
#greet=stars(uppercase1(greet))
print("after 'greet'")

result=greet("Dangerous Dan", punctuation1="!!")
print (result)
def v_function():
  print("inside 'v_function'")
  return "Hello World"
stars(uppercase1(v_function))
uppercase1(stars(v_function))