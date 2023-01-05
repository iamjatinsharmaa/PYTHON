#import pandas as pd

#pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

jatinsApplication = RailwayForm()
jatinsApplication.name = "Jatin"
jatinsApplication.train = "Rajdhani Express"
jatinsApplication.printData()