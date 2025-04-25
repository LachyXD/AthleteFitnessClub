import datetime as dt
import json

class Reciept:
    def __init__(self):
        self.data = None

    def setData(self, data: dict):
        self.data = data

    def calcTotal(self):
        total = 0.00
        for description, amount in self.data.items():
            if description != "Name" and description != "Weight":
                total += amount

        self.data["Total"] = total

    def create(self):
        with open("Reciept.json", "w") as reciept:
            json.dump(self.data, reciept)

    def display(self):
        with open("Reciept.json", "r") as reciept:
            output = json.load(reciept)
            print("##### RECIEPT #####")
            for description, amount in output.items():
                if description != "Name" and description != "Weight":
                    print(f"{description} @ £{amount:.2f}")
                else:
                    print(f"{description}: {amount}") #amount in this case is the name or weight