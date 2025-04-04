from user import *
from training import *

#Config
privFee = 9.50 #hourly rate
compFee = 22.00
#Format 0. Weight category name, 1. min weight, 2. max weight
categoryComp = [["Heavyweight", 101, 999],["Light-Heavyweight", 90,100],["Middleweight", 82,90],["Light-Middleweight", 74,81],["Lightweight", 67,73],["flyweight", 0,66]]
costs = []

#Creates the athlete profile
print("##### ATHLETE DETAILS #####")
person = Athlete()
person.getName()
person.getWeight()

#Training Plan
trainingPlan = Training()
trainingPlan.setPlan()
costs.append([f"Training Plan ({trainingPlan.getPlan()})",trainingPlan.getCost()])

#Output of costs
person.displayInfo()
print("##### RECIEPT #####")
for cost in costs:
    print(f"{cost[0]} @ £{cost[1]:.2f}")