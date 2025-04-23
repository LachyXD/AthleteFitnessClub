from user import *
from training import *
from competition import *
from reciept import *

#Config
costs = []

#Creates the athlete profile
print("##### ATHLETE DETAILS #####")
person = Athlete()
person.getName()
person.setWeight()

#Training Plan
trainingPlan = Training()
trainingPlan.setPlan()
person.setPlan(trainingPlan.getPlan())
costs.append([f"Training Plan ({trainingPlan.getPlan()})",trainingPlan.getCost()])

#Competitions
compete = Competitions()
compete.eligibilityChecker(trainingPlan.getPlan())
compete.enter()
costs.append([f"{compete.getCount()} {compete.getCategory()} Competitions", compete.getCost()])
person.setCategory(compete.getCategory())
compete.weightCompare(person.getWeight(), compete.getCategory())

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
reciept = Reciept()
reciept.setCosts(costs)
reciept.makeReciept(person)
