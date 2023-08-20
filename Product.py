"""
Create Product class,
each product has name, category, and price---> instance variable
class is able to return a discription of product --> method
for each product be able to compute discount of a given amount
(compute price after discount of amount %)
"""
class Product:
    #self pointing like this
    #constructor
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getPrice(self):
        return self.price
        
    def setName(self, newName):
        self.name = newName  #newName from user
        
    def descrip(self):
        return f"Product: {self.name} is {self.category} cost {self.price}"
    
    #discount
    def discount(self, amount):
        self.price = self.price - (self.price * amount/100)
        if self.category == "Electronics":
            self.price += 10
        
  
    