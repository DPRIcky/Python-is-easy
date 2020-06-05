class pet:
    def __init__(self,name,a,h,p):
        self.name = name
        self.age = a
        self.hunger = h
        self.playful = p

    # getters #
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getHunger(self):
        return self.hunger
    
    def getPlayful(self):
        return self.playful

    # setter #
    def setName(self,xname):
        self.name = xname
    
    def setAge(self,age): 
        self.age = age
    
    def setHunger(self,hunger):
        self.hunger = hunger

    def setPlayful(self,play):
        self.playful = play

class dog(pet):
    def __init__(self,name,age,hunger,playful,breed,toy):

        pet.__init__(name,age,hunger,playful)
        self.breed = breed
        self.toy = toy

    