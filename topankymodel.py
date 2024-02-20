class Shoe:
    def __init__(self, id, gender_type,type,colour,size,brand,price):
        self.id = id
        self.gender_type = gender_type
        self.type = type
        self.colour = colour
        self.size = size
        self.brand = brand
        self.price = price

class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self,shoe):
      if any(s.id==shoe.id for s in self.shoes):
          print("Tovar s tymto ID uz existuje")
          return False
#         for a in self.shoes:
#             if a.id==shoe.id:
#                 print("Tovar s tymto ID uz existuje")
#                 return False
      if shoe.price<0:
         print("Uvedna cena je zaporna")
         return False
      self.shoes.append(shoe)
      return True

    def remove_shoe(self,id):
        self.shoes=[s for s in self.shoes if s.id !=id]

    def get_shoes(self):
        return self.shoes

    def get_shoes_size(self,size):
        return [c for c in self.shoes if c.size==size]

    def get_price(self):
        return sum(d.price for d in self.shoes )













