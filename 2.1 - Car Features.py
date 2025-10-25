'''Car with make, model, year as attributes, and start(), stop() as methods'''
class Car :
    def __init__ (self, company, model, year) :
        self.company=company
        self.model=model
        self.year=year
    def display (self) :
        print("The car is of model ", self.model, " manufactured by ", self.company, " in the year ", year)
    def start (self) :
        print("The car is started.")
    def stop (self) :
        print("The car is stopped.")
company=input("Enter the name of the company of the car: ")
model=input("Enter the name of the model of the car: ")
year=int(input("Enter the year the car was manufactured: "))
c=Car(company, model, year)
c.display()
c.start()
c.stop()
