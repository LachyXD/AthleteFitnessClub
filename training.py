class Training:
    def __init__(self):
        self.trainingPlans = {"B": ("Beginner", 25.00), "I": ("Intermediate", 30.00),"E": ("Elite", 35.00)}
        self.planChoice = ""
    
    def setPlan(self):
        #Allow user to select training plan
        print("##### TRAINING PLANS #####")
        for code, (plan, price) in self.trainingPlans.items():
            print(f"{code}: {plan} £{price}")

        #validation loop
        while True:
            self.planChoice = input("Select a plan using the name or first letter: ")
            if self.planChoice.capitalize() in self.trainingPlans:
                break
            else:
                print("Invalid choice")

    def getCost(self):
        #Add training fee 
        plan = self.trainingPlans.get(self.planChoice.capitalize())
        return plan[1]
            
    def getPlan(self):
        return self.planChoice
    
#private training
class PrivTuition:
    def __init__(self):
        self.hours = 0
        self.fee = 9.50

    def hoursTuition(self):
        print("##### PRIVATE TUITION #####")
        while True:#tuition validation loop
            try:
                self.hours = int(input("How many hours of private tuition would you like a week (max 5) "))
                if self.hours >5:
                    print("too much private tuition. try again")
                elif self.hours <0:
                    print("cannot have negative hours")
                else:
                    break
            except ValueError:
                print("Invalid input type, enter a number...")
        
        totalFee = (self.hours *4) * self.fee
        return totalFee
    
    def getHours(self):
        return self.hours