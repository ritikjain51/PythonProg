'''
class class_name(object):

    def __init__(self, a):
        self.a = a

    def func_name (self, parameter):
        some code
        return

    def __str__(self):
        return 'String'


I have a class named person which have
Attributes:
    Name
    Gender
    Age

Methods:
    Constructor
    put_name
addr    put_gen
    put_age
    get_name
    get_age
    get_gender
    display function
'''


class Person(object):

    def __init__(self, name, gen, age):

        self.name = name
        self.gender = gen
        self.age = age

    def put_name (self, name):
        self.name = name

    def put_gender(self, gen):
        self.gender = gen

    def put_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def isEmployee(self):
        return False
    
    def __str__(self):
        return f'Name: {self.name} Gender: {self.gender} Age: {self.age}'

    def __repr__(self):
        return f'Name: {self.name} Gender: {self.gender} Age: {self.age}'



'''
Employee class
Attributes:
    Name
    Gender
    Age
    ID Number

Methods:
    Constructor
    put_name
    put_gen
    put_age
    get_name
    get_age
    get_gender
    isEmployee
    display function
'''

class Employee(Person):

    def __init__(self, name, gender, age, id):
        Person.__init__(self, name, gender, age)
        self.id = id
        
    def isEmployee(self):
        return True

    def put_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
    def __str__(self):
        return f'Name: {self.name} Gender: {self.gender} Age: {self.age} Id: {self.id}'

    def __repr__(self):
        return f'Name: {self.name} Gender: {self.gender} Age: {self.age} Id: {self.id}'
 



'''
Task 
You have a class named School define all the attributes and methods
You have another class Teacher which inherit School class
You have another class Student which inherit School Class
'''
