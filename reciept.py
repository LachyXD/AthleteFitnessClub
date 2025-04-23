import datetime as dt

class Reciept:
    def __init__(self):
        self.costs = None

    def setCosts(self, costs):
        self.costs = costs

    def makeReciept(self, athlete):
        with open("Reciept.txt", "w") as reciept:
            reciept.write(f"##### RECIEPT FOR {dt.datetime.now()} #####")
            reciept.write(f"{athlete.displayInfo()}\n")
            for description, amount in self.costs.items():
                reciept.write(f"{description} @ £{amount:.2f}\n")