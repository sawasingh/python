class Fraction:
    def __init__(self,n,d):
        self.n = n
        self.d = d

    def __str__(self):
        return "{}/{}".format(self.n,self.d)
    
    def __add__(self,other):

        temp_num = self.n * other.d + self.d * other.n
        temp_den = self.d * other.d
    
        return Fraction(temp_num, temp_den)

    def __mul__(self,other):
        temp_num = self.n * other.n
        temp_den = self.d * other.d

        return Fraction(temp_num,temp_den)

    def __truedivc__(self,other):
        temp_num = self.n * other.d
        temp_den = self.d * other.n

        return Fraction(temp_num,temp_den)


    

x =  Fraction(4,2)
y = Fraction(4,5)
print(x+y)
print(x*y)
print(x/y)

