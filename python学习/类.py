class Calculator:
    def __init__(self,name,price,hight, width,weight):
        self.name=name
        self.price=price
        self.h=hight
        self.wi=width
        self.we=weight#自己输入属性
    def add(self,x,y):
        result = x+y
        print(self.name)
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)


c=Calculator('Bad calcuator',12,30,15,19)
c.name
c.add(8,12)
c.times(12,3)

a=[1,2,3,4,2,3,1,1]

a.insert(1,0)
print(a)
a.remove(2)
print(a)
