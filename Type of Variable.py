""" Inside a class basically we have 3 type of variable.
public: anywhere, anyone can use it. Inside or outside the class.
protected: we protect our variable or method inside the class. (By default object do not provide the suggestion.)
private: we can decelare our method or variable inside the class as private. No one can use directly, first they have to reachout to class.
"""

class person:

    def __init__(self,name,surname,dob):

        self.name=name                              # Public variable
        self._surname=surname                  # Protected variable
        self.__dob=dob                                # Private variable

    def test(self):                                        # Public method/Function
        return ("Print the name of person",self.name)

    def _test1(self):                                   # Protected method/Fucntion
        return ("Print the surname of person",self._surname)

    def __age(self,current_year):           # Private method/Function

        a= current_year - self._person__dob
        return  a

obj=person("anubhav","kumar",1994)

print(obj.name)                 # We can access public variable directly, via the help of class object.
print(obj._surname)          # Suggestion is not available. If you want to use protect variable provide the _ and variable name.
print(obj._person__dob)   # First you have to write the class name after that variable name. Without using class name you can't access private variable.

print(obj.test())
print(obj._test1())
print(obj._person__age(2022))    # Same process work of method/function as well.
                                                    # We have public, protected and private method as well.
