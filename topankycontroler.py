

class ShoeController:
    def __init__(self,model,view):
        self.model=model
        self.view=view

    def add_shoe(self,id,gender_type,type,colour,size,brand,price):
        shoe=Shoe(id,gender_type,type,colour,size,brand,price)
        if self.type.add_shoe(shoe):
            print("Topanky boli pridane")
        else:
            print("Topanky neboli pridane")

    def remove_shoe(self, id):
        self.typ.remove_shoe(id)
        print("Topanky boli vymazane")

    def show_shoes(self):
        shoes=self.type.get_shoes()
        ShoeView.display_shoes(shoes)

    def show_shoes_size(self,size):
        shoes=sellf.type.get_shoes_size(size)
        ShoeView.display_shoes(shoes)

    def show_total_price(self):
        total_price=self.type.get_price()
        print("Celkova cena topanok:",total_price)


