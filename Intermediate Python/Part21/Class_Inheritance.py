class Animal:
    def __init__(self, num):
        self.num_eyes=num #without any argument passing the init funtion in the base class can  be omitted, incase it is not needed by iy
    def breath(self):
        print("Inhale Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__(2) #whether argument is present or not this is mandatory
    def breath(self):
        super().breath()
        print("doning under water")
    def swim(self):
        def swim(self):
            print("moving in water")

g1=Fish()
g1.breath()
g1.swim()

