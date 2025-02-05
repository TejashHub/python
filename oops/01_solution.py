class Car:

    total_car = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.brand
    
    @property
    def get_model(self):
        return self.__model
    
    def info(self):
        result = f"Presenting the {self.brand} {self.__model} - a perfect fusion of style, innovation, and performance!"
        return result
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    def __str__(self):
        return self.info()

class Bettery:
    def __init__(self, battery_model):
        self.battery_model = battery_model  

    def bettery_info(self):
        return f'Bettery Model is {self.battery_model}'

class Engine:
    def __init__(self, engine_model):
        self.engine_model = engine_model  

    def engine_info(self):
        return f'Engine Model is {self.engine_model}'

class ElectricCar(Car, Bettery, Engine):
    def __init__(self, brand, model, battery_model, engine_model):
        Car.__init__(self, brand, model)
        Bettery.__init__(self, battery_model)  
        Engine.__init__(self, engine_model)    

tesla = ElectricCar("Tesla", "Model S", "Tesla Battery X", "Tesla Engine Y")
print(tesla.info())
print(tesla.bettery_info())
print(tesla.engine_info())
