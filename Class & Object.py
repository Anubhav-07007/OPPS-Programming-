"""OOPS is object oriented programing. Where we create the class and object.

Class : In a  simple words class is a classification. its a blueprint of real life.
Object: by the help of object we can use the class method or variable.
pointer : Self is a by default pointer. By the help of pointer class can identify, what and how many method & variable assign to it.

"""

class person:    # Create a person Class

    def __init__(self,name,surname,dob):  # Create a variable with in the class.
        self.name=name
        self.surname=surname
        self.dob=dob

    def age(self,current_year):
        "This function calculate the age of person"


        a=current_year - self.dob
        return  a

obj=person("anubhav","kumar",1994)    # Create a obj for a class.

print(obj.age(2022))                            # By the help of object we can call it any method or variable inside the class.

print(obj.name)
print(obj.dob)
print(obj.surname)

