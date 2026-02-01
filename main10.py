# dataclasses is module decorator-boilerplate code
# to store data with classes primarily designed...
#__init__(),__repr__()=string, __eq__()=comparison

from dataclasses import dataclass

@dataclass
class Point:
    cx:int
    cy:int
p= Point(2,5)

print(p)