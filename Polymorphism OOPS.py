""" Polymorphism: In simple words we can say that as per sistuation the behaviour of function will change accordingly.
example: we can create multiple class and the method of every class is same. but via using polymorphism we can access all method outside the class.
"""


class ineuron:

    def students(self):
        print("Print a student details")

class class_type:
    def students(self):
        print("print the class type of students")


def ineuron_external(a):
    a.students()

i=ineuron()
j=class_type()

ineuron_external(i)
ineuron_external(j)

def test(a,b):
    return a+b

print(test(2,4))
print(test("anubhav","kumar"))