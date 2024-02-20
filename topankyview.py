
class ShoeView:
    @staticmethod
    def display_shoes(shoes):
        if not shoes:
            print("Ziadne topanky ")
            return
        print("ID\Gender_type\Type\Colour\Size\Brand\Price")
        for shoe in shoes:
            print(f"{shoe.id}\{shoe.Gennder_type}\{shoe.Type}\{shoe.Colour}\{shoe/Size}\{shoe.Brand}\{shoe.Price}")

