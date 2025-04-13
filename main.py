from user import *
from training import *
from competition import *

#Config
#Format 0. Weight category name, 1. min weight, 2. max weight
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

#Competitions
compete = Competitions()
compete.eligibilityChecker(trainingPlan.getPlan())
compete.enter()
costs.append([f"{compete.getCount()} Competitions", compete.getCost()])

#Private Tuition Section
privTuition = PrivTuition()
privFee = privTuition.hoursTuition()
costs.append([f"Private Tuition {privTuition.getHours()} weekly hours", privFee])

#Output of costs
person.displayInfo()
print("##### RECIEPT #####")
for cost in costs:
    print(f"{cost[0]} @ £{cost[1]:.2f}")

#Write to file
