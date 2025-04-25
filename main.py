from user import *
from training import *
from competition import *
from reciept import *

#Config
data = {}

#Creates the athlete profile
print("##### ATHLETE DETAILS #####")
person = Athlete()
person.setName()
person.setWeight()
data[f"Name"] = person.getName()
data[f"Weight"] = f"{person.getWeight()} KG"

#Training Plan
trainingPlan = Training()
trainingPlan.setPlan()
person.setPlan(trainingPlan.getPlan())
data[f"Training Plan ({trainingPlan.getPlan()})"] = trainingPlan.getCost()

#Competitions
compete = Competitions()
compete.eligibilityChecker(trainingPlan.getPlan())
compete.enter()
data[f"{compete.getCount()} {compete.getCategory()} Competitions"] = compete.getCost()
person.setCategory(compete.getCategory())
compete.weightCompare(person.getWeight(), compete.getCategory())

#Private Tuition Section
privTuition = PrivTuition()
privFee = privTuition.hoursTuition()
data[f"Private Tuition {privTuition.getHours()} weekly hours"] = privFee

#Output of costs saves and loads to/from a json file
reciept = Reciept()
reciept.setData(data)
reciept.calcTotal()
reciept.create()
reciept.display()