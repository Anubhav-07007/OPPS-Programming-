""" Inheritance is widly use inside the oops programming. By the help the of inheritance we don't wirte the same code again & again.
we can inherit the method or code from different class. We can increase the re-usability of code.

Multilevel Inheritance: A class can also b used in one class. which is already be used in another class.
Multiple Inheritnace: We can define multiple class and use those class in singel class.
Data Abstraction(Hiding) : In a simple word. We can hide our variable or method behind the class. (Private variable/method)
Data Encapsulation(modefiy) : If the variable is public. we can update the value of variable via the help of class object.
                                    But if the variable is private, we can't update the value of variable. We can do that by the help of setter method.
                                    Means first we have to create a setter method and update the value over there.
"""


# Multilevel Inheritance:

class private_bank:

    def hdfc_account(self):
        return  ("Account openining process in pnb bank")

    def citi_bank(self):
        return ("Account openining process in citi bank")

class goverment_bank(private_bank):

    def pnb_account(self):

        return ("Account openining process in pnb bank")

    def sbi_account(self):

        return ("Account openining process in sbi bank")

class all_bank(goverment_bank):    # Here we use multilevel inheritance. Goverment bank is already inherit property from private bank
          pass                                              # Goverment bank already have all method use in private bank.



obj_all_bank=all_bank()

print(obj_all_bank.citi_bank())
print(obj_all_bank.hdfc_account())
print(obj_all_bank.sbi_account())
print(obj_all_bank.pnb_account())


#  Multiple Inheritance:

class student:

    def __init__(self,stud1,stud2,stud3):
        self.stud1=stud1
        self.stud2=stud2
        self.stud3=stud3

class school_class:

    def Class1(self):
        return ("Students from class 1")

    def Class2(self):
        return ("Students from class 2")

class school(school_class,student):
    pass

obj_school=school("anu","kanu","priya")

print(obj_school.stud1)
print(obj_school.Class1())


#  Data Abstraction

class person:

    __age=1994                  # Define private variable

    def __find_age(self,current_age):  # Define private method.. without using class name we can't access the method.

        a= current_age - self._person__age

        return  a

obj_person=person()

print(obj_person._person__find_age(2022))   # example of data abstraction.


# Data encapsulation

class ineuron:

    students="Data Science"

    def test(self):

        return (self.students)

obj1=ineuron()

print(obj1.test())

obj1.students="Big Data"         # if define the public variable we can change the variable value via using class object.

print(obj1.test())

class ineuron_test:

    __students1="data science"

    def test1(self):
        return (self._ineuron_test__students1)

    def change_value(self,new_value):
        self.__students1=new_value

obj2=ineuron_test()

print(obj2.test1())

obj2.__students1="big data"

obj2.change_value("anubhav")

print(obj2.test1())