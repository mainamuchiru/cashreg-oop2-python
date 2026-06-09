#!/usr/bin/env python3

class CashRegister:
  pass
  
  def __init__(self,discount):
    self.discount = discount
    
    self.total = 0
    self.items = []
    self.previous_transactions = []
    
    @property
    def discount (self):
       return self.discount
     
    @property.setter
    def discount(self, value):
      if value == range(0, 100):
        self.discount =  value
      else:
        print("Not valid discount.")
    
    def add_item(self,item, price, quantity):
        price = self.total 
      
        if item not in self.item:
            self.item.append(item)
        
        quantity = {
            "item": item,
            "price": price,
            "quantity": quantity
            }
        self.previous_transactions.append(quantity)
        
    def apply_discount():
        discount = self.total*self.discount
        del self.previous_transactions[-1] 
        
        if not self.previous_transactions:
          print("There is no discount to apply.”")
 
    