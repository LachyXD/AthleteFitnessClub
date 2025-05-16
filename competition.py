class Competitions:
    def __init__(self):
        #format category name, min weight, max weight
        self.categories = [["Heavyweight", 101, 999],["Light-heavyweight", 90,100],["Middleweight", 82,90],["Light-middleweight", 74,81],["Lightweight", 67,73],["Flyweight", 0,66]]
        self.fee = 22.00
        self.entries = 0
        self.eligible = False
        self.category = ""
        #Dict for categories
        self.categoryMap = {cat[0]: (cat[1],cat[2] ) for cat in self.categories}

    def eligibilityChecker(self, athleteTrainingPlan: str):
        enter = input("Would you like to enter competitions? Y or N\n")
        if enter.upper() == "Y" and athleteTrainingPlan.upper() in ["I","E", "ELITE", "INTERMEDIATE"]:
            self.eligible = True

    #this allows the user to enter competitions or to deny their entry if they are on the incorrect membership plan
    def enter(self):
        if self.eligible:
            for category, (minWeight, maxWeight) in self.categoryMap.items():
                print(f"{category} Min Weight: {minWeight}kg Max Weight {maxWeight}kg")

            while True:
                categoryChoice = input("Select a weight category: ")
                if categoryChoice.capitalize() in self.categoryMap: #uses the dict created to look at all the keys to check for matches.
                    break
                else:
                    print("Invalid weight category")

            self.category = categoryChoice.capitalize()

            while True: #Validation Loop for entering competions to ensure only integers are entered.
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

    #Getters and setters
    def getCost(self):
        cost = self.entries * self.fee
        return cost
    
    def getCount(self):
        return self.entries
    
    def getCategory(self):
        return self.category
    
    #Weight Comparison System
    def weightCompare(self, athleteWeight :float, athleteCategory: str):
        if athleteCategory != "":
            
            if athleteCategory.capitalize() in self.categoryMap:
                catMinWeight, catMaxWeight = self.categoryMap[athleteCategory.capitalize()]

            if athleteWeight > catMaxWeight:
                difference = athleteWeight - catMaxWeight
                print(f"{difference}KG Overweight!")
            elif athleteWeight < catMinWeight:
                diffrence = catMinWeight - athleteWeight
                print(f"You need to gain {diffrence}KG")
            else:
                print("As it stands you will make weight!")