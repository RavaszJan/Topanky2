# Topanky2

# if __name__=="__main__"
from  topankycontroler import ShoeController
from topankymodel import ShoeModel
from topankyview import ShoeView


model=ShoeModel()
view=ShoeView()
controller=ShoeController(model,view)




    controller.add_shoe(1,"Panske","Nike Air MAx","Modra",43,"Nike",140)
    shoe_controller.add_shoe(2,"Zenske","Nike Air MAx","Fialova",39,"Nike",145)

    shoe_controller.show_shoes()
    shoe_controller.show_shoes_size(39)
    shoe_controller.show_total_price()
    shoe_controller.remove_shoe(1)

controller.display_shoes()




