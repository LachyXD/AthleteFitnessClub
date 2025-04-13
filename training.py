class Training:
    def __init__(self):
        self.trainingPlans = [["B","Beginner", 25.00], ["I","Intermediate", 30.00], ["E","Elite", 35.00]]
        self.planChoice = ""
    
    def setPlan(self):
        #Allow user to select training plan
        print("##### TRAINING PLANS #####")
        for plan in self.trainingPlans:
            print(f"{plan[1]} £{plan[2]}")

        #validation loop
        while True:
            self.planChoice = input("Select a plan using the name or first letter: ")
            if self.planChoice.capitalize() in [self.trainingPlans[0][0], self.trainingPlans[0][1], self.trainingPlans[1][0], self.trainingPlans[1][1], self.trainingPlans[2][0], self.trainingPlans[2][1]]:
                break
            else:
                print("Invalid choice")

    def getCost(self):
        #Add training fee 
        for plan in self.trainingPlans:
            if self.planChoice.capitalize() in [plan[0], plan[1]]:
                trainingFee = plan[2]
                return trainingFee
            
    def getPlan(self):
        return self.planChoice
    
#private training
class PrivTuition:
    def __init__(self):
        self.hours = 0
        self.fee = 9.50

    def hoursTuition(self):
        print("##### PRIVATE TUITION #####")
        while True:
            try:
                self.hours = int(input("How many hours of private tuition would you like a week (max 5)"))
                if self.hours > 5:
                    print("too much private tuition. try again")
                else:
                    break
            except ValueError:
                print("Invalid input type, enter a number...")
        
        totalFee = (self.hours *4) * self.fee
        return totalFee
    
    def getHours(self):
        return self.hours