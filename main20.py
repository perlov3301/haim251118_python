import time
import math
print("main20;real world example")
def stopper(func):#measuring execution time
  def inner (*args, **kwargs):#inner function is invoked
    start=time.perf_counter()
    value=func(*args, **kwargs)
    end=time.perf_counter()
    run= end- start
    print(f"running time= {round(run,3)}sec")
    return value
  return inner
@stopper
def doSomething(*args, **kwargs):
  a=10.0
  b=20.0
  c=0.0
  i=0
  for i in range(kwargs["times"]):
    c=a+b
    # print(i)
  return i
doSomething(times=36300000)

def arithm1(a:float,b:float, c:str):
  if c=="+":
    return a+b
  elif c=="-":
    return a-b
  elif c=="*":
    return a*b
  elif c=="/":
    return a/b
  elif c=="%":
    return a%b
  elif c=="**":
    return a**b
def v_check1():
  a=4
  b=5
  c=0
  n=1
  for n in range(1,36300001):
    c= a+b
  return round(n/1000000,1)
start1= time.perf_counter_ns()
result1= arithm1(math.pi, 3, "**")
end1= time.perf_counter_ns()
run1= end1-start1
print(f"result={result1} running time is {run1}nS")
start1= time.perf_counter()
result1= v_check1()
end1= time.perf_counter()
run1= end1-start1
print(f"n={result1}mln running time is {run1}sec")



