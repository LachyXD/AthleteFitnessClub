class Athlete:
    def __init__(self):
        self.name = ""
        self.plan = ""
        self.weight = 0.00
        self.category = ""

    def setName(self):
        self.name = input("Please Enter your name: ")

    def getName(self):
        return self.name
    
    def setPlan(self, plan: str):
        self.plan = plan

    def setWeight(self):
        while True:
            try:
                self.weight = float(input("Please enter your weight in kg: "))
                break
            except ValueError:
                print("input must be a float")
            except:
                print("An unknown error occured")

    def getWeight(self):
        return self.weight
    
    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Weight: {self.weight}kg")
        print(f"Training plan: {self.plan}")

    #get weight category
    def setCategory(self, category: str):
        self.category = category