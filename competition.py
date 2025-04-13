class Competitions:
    def __init__(self):
        #format category name, min weight, max weight
        self.categories = [["Heavyweight", 101, 999],["Light-Heavyweight", 90,100],["Middleweight", 82,90],["Light-Middleweight", 74,81],["Lightweight", 67,73],["flyweight", 0,66]]
        self.fee = 22.00
        self.entries = 0
        self.eligible = False

    def eligibilityChecker(self, athleteTrainingPlan):
        enter = input("Would you like to enter competitions? Y or N\n")
        if enter.upper() == "Y" and athleteTrainingPlan.upper() in ["I","E", "ELITE", "INTERMEDIATE"]:
            self.eligible = True

    def enter(self):
        if self.eligible:
            for category in self.categories:
                print(f"{category[0]} Min Weight: {category[1]}kg Max Weight {category[2]}kg")

            while True:
                categoryChoice = input("Select a weight category: ")
                if categoryChoice.capitalize() in [self.categories[0][0], self.categories[1][0], self.categories[2][0], self.categories[3][0], self.categories[4][0], self.categories[5][0]]:
                    break
                else:
                    print("Invalid weight category")

            while True:
                try:

                    self.entries = int(input(f"Enter how many competitions you would like to enter (£{self.fee} each): "))
                    
                    if self.entries >= 0:
                        break
                    else:
                        print("Cant enter negative competitions!")
                except:
                    print("Input must be a number")
        else:
            print("You are not eligible to enter competitions on current membership plan")

    
    def getCost(self):
        cost = self.entries * self.fee
        return cost
    
    def getCount(self):
        return self.entries