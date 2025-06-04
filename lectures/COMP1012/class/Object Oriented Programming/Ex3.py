'''
The __str__() Function

The __str__() function controls what should be returned when the 
class object is represented as a string.

If the __str__() function is not set, the string representation of the
 object is returned:
'''
#Without --Str--
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1) 

#With --Str--

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) 