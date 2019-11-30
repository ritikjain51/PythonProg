##'''
##Operator Overloading
##
##It is a feature of Polymorphism. It uses the normal operators to be overloaded
##and return the result.
##
##'''
##
##
##class Number (object):
##
##    def __init__(self, a, b, c):
##
##        self.a = a
##        self.b = b
##        self.c = c
##
##    ## Creating a function named checkGreater
##    def check_greater(self, obj1):
##        if (self.a > obj1.a):
##            if (self.b > obj1.b):
##                if (self.c > obj1.c):
##                    return True
##    
##        return False
##
##    def __gt__(self, obj1):
##        if (self.a > obj1.a):
##            if (self.b > obj1.b):
##                if (self.c > obj1.c):
##                    return True
##    
##        return False
##
##    def __add__(self, obj):
##        n = Number(0, 0, 0)
##        n.a = self.a + obj.a
##        n.b = self.b + obj.b
##        n.c = self.c + obj.c
##        return n
##
##n1 = Number(4,5,6)
##n2 = Number (3,2,4)
##print (n1.check_greater(n2))
##
##print (n1 > n2)



class Complex(object):

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, obj):
        real = self.real + obj.real
        img = self.img + obj.img
        return Complex(real, img)

    def __repr__(self):
        return f'{self.real}+{self.img}i'

    def __sub__(self, obj):
        real = self.real - obj.real
        img = self.img - obj.img
        return Complex(real, img)

    def __mul__(self, obj):
        real = self.real * obj.real
        img = self.img * obj.img
        return Complex(real, img)

    def __gt__(self, obj):
        pass

    def __lt__(self, obj):
        pass

    def __div__(self, obj):
        pass

    
c1 = Complex(5, 4)
c2 = Complex(6, 4)
c3 = c1 + c2
c4 = Complex(3, 2)



