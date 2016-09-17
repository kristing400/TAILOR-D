from flask_api import FlaskAPI
import random
import copy

class Database(object):
    def __init__(self):
        self.db = dict() #store by id
        self.colors = dict() 
        self.lookup_table = dict() #store by type

    def deleteAll(self):
        self.db = dict()

    def store_clothe(self, clothe_info):
        pic, color, color_hex, clothe_type, season, clothe_id = clothe_info
        clothe_d = {
            "pic": pic ,
            "color": color ,
            "hex": color_hex,
            "type": clothe_type ,
            "season": season , 
            }
        self.db[clothe_id] =clothe_d
        if clothe_type not in self.lookup_table:
            self.lookup_table[clothe_type] = [clothe_id]
        else:
            self.lookup_table[clothe_type].append(clothe_id)

        return clothe_id

    def get_clothe_by_type(self, choice):
        return self.lookup_table[choice]

    def get_hex(self, clothe_id):
    	return self.db[clothe_id]["hex"]



def generate(db):
    found = False
    matched_top = None
    matched_bottom = None
    matched_colors = None
    while not found:
        rand_top = random.choice(db.get_clothe_by_type("top")) #returns id
        matched_top = rand_top
        # top_color = db.db[rand_top]["color"]
        top_hex = db.db[rand_top]["hex"]
        colors_to_match = None
        palettes_temp = copy.deepcopy(db.colors)
        while len(palettes_temp) > 0:
            #assume we always find color
            rand_palette = random.choice(palettes_temp)
            palettes_temp.remove(rand_palette)
            print rand_palette
            if top_hex in rand_palette:
                matched_colors = copy.deepcopy(rand_palette)
            if matched_colors != None:
                for bottom in db.get_clothe_by_type("bottom"):
                    bottom_hex =db.get_hex(bottom)
                    if (bottom_hex in matched_colors) and (bottom_hex != top_hex):
                        found = True
                        matched_bottom = bottom

   
    return matched_top, matched_bottom, matched_colors










test = Database()
clothetest = ("01.png","white","0x44","top","summer","01")
clothetest1 = ("01.png","black","0x22","bottom","summer","02")
palletes = [['0x43', '0x243'], ['0x23','0x11'], ['0x44','0x22'] ]
test.colors = palletes
test.store_clothe(clothetest)
test.store_clothe(clothetest1)
print test.db
print test.lookup_table
print generate(test)
# app = FlaskAPI(__name__)





# @app.route('/', methods=['GET'])
# def test():
#     return {'hello': 'world'}
