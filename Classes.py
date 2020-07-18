class Dog:
    
    #cosntructor
    def __init__(self,breed):
        self.breed = breed
    #Method
    def bark(self):
        print("howwww bhowwww")
    
    def intro_of_dog(self):
        print(f"This is {self.breed}")
    
    #def color(self):
    #    print("Red")
    
    
    #def manufactured_year(self):
    #    print("2010")

maxi = Dog("German Shephered")
russian = Dog ("Bull dog")

maxi.intro_of_dog()
maxi.bark()
russian.intro_of_dog()
russian.bark()
    
