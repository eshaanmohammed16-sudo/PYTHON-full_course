class cat:
    def __init__(self, name , breed):
        self.name=name
        self.age=0
        self.breed=breed
        self.dob=0
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getbreed(self):
        return self.breed
    def getdob(self):
        return self.dob
    def setname(self , name):
        self.name = name
    def setage(self , age ):
        self.age =age
    def setbreed(self , breed):
        self.breed = breed
    def setage(self , dob ):
        self.dob =dob
class kitten(cat):
    def __init__(self , name, breed , playfulness ):
        super().__init__(name , breed)
        self.playfulness=playfulness
    def getplayfulness(self):
        return self.playfulness
    def setplayfulness(self):
        self.playfulness=playfulness
kitten1=kitten("kit", " cat" , 0)
print(kitten1.getname())