from user import *

#Config
trainingPlans = [["B","Beginner", 25.00], ["I","Intermediate", 30.00], ["E","Elite", 35.00]]
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

#Allow user to select training plan
print("##### TRAINING PLANS #####")
for plan in trainingPlans:
    print(f"{plan[1]} £{plan[2]}")

#validation loop
while True:
    planChoice = input("Select a plan using the name or first letter: ")
    if planChoice.capitalize() in [trainingPlans[0][0], trainingPlans[0][1], trainingPlans[1][0], trainingPlans[1][1], trainingPlans[2][0], trainingPlans[2][1]]:
        break
    else:
        print("Invalid choice")

#Add training fee 
for plan in trainingPlans:
    if planChoice.capitalize() in [plan[0], plan[1]]:
        trainingFee = plan[2]
        costs.append(["Training Plan", trainingFee])

#Output of costs
person.displayInfo()
print("##### RECIEPT #####")
for cost in costs:
    print(f"{cost[0]} @ £{cost[1]:.2f}")