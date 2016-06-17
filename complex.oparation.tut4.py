#Complex Number: additaion, subtraction, multiplication and division
import numpy as ben
class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
    def __div__(self, other):
        return Complex((self.real*other.real + self.imag*other.imag)/(other.real**2+other.imag**2),
                       (self.imag*other.real-self.real*other.imag)/(other.real**2+other.imag**2))
    def __str__(self):
        return '(%g,%g)'%(self.real,self.imag)
    
comp1 = Complex(7.0,6.0)
comp2 = Complex(5.0,-2.0)
complxsum = comp1 + comp2
thedif = comp1 - comp2
thepro = comp1*comp2
thequs = comp1/comp2
print (comp1)
print  (comp2)
print  (complxsum)
print  (thedif)
print  (thepro)
print  (thequs)
    

