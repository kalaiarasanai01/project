# single inheritance
'''class dad():
    def phone(self):
        print("Dad's Phone")
class mom():
    def mobile(self):
     print("iphone")
                
class son(dad,mom):
    def laptop(self):
        print("son's laptop")
kalai = son()
kalai.laptop()  
kalai.phone()
kalai.mobile()'''

# multilevel inheritance

'''class grandpa():
    def land(self):
        print('Owner of the land')
class father(grandpa):
    def car(self):
        print('Drive a car')
class son(father):
    def bike(self):
        print('racer')
biker = son()
biker.land()
biker.car()
biker.bike()'''
#hireacky inheritance

'''class dad():
    def money(self):
        print('Sharing money')
class son1(dad):
    pass
class  son2(dad):
    pass
class son3(dad):
    pass
s1 = son1()
s1.money()
s2 = son2()
s2.money()
s3=son3()
s3.money()'''
#hybrid inheritence

class dad ():
    def car (self):
        print('New car')
class uncle():
    def bike (self):
        print('win the race')
class Ramu(dad):
    pass
class Raju(dad):   
    pass
class Ravi(uncle):
    pass
Elder_brother = Ramu()
Elder_brother.car()
Younger_brother = Raju()
Younger_brother.car()
cousin = Ravi()
cousin.bike()








