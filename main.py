class Car:
    def __init__ (self, model, year, manufacturer, engine, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def showMsg(self):
        print(f"Model: {self.model}   Rok výroby: {self.year} Výrobce: {self.manufacturer} Objem motoru: {self.engine} cm3 Barva: {self.color} Cena: {self.price}")

car1 = Car("Yaris", 2010, "Toyota", 1.5, "White", 300000)
car1.showMsg()
print(car1.year)