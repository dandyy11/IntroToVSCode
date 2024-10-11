
import random


class Insect:
    
    def __init__(self,w,l,name):
        self.wings = w  
        self.legs = l  
        self.flight = 0 
        self.name = name

 
    def calc_flight(self):
        self.flight = random.randint(1, 10)  

   
    def get_flight(self):
        return self.flight

  
    def get_flight(self):
        return self.name
    
    def get_name(self):
        return self.name
