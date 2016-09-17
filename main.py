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
    
    def get_pic(self, clothe_id):
    	return self.db[clothe_id]["pic"]
app = FlaskAPI(__name__)
_db = Database()
clothetest = ("01.png","white","0x44","top","summer","01")
clothetest1 = ("02.png","black","0x22","bottom","summer","02")
_db.store_clothe(clothetest)
_db.store_clothe(clothetest1)


palletes = [['0x43', '0x243'], ['0x23','0x11'], ['0x44','0x22'] ]
_db.colors = palletes

@app.route('/generate', methods=['GET'])
def generate():
    found = False
    matched_top = None
    matched_bottom = None
    matched_colors = None
    while not found:
        rand_top = random.choice(_db.get_clothe_by_type("top")) #returns id
        matched_top = rand_top
         top_hex = _db.db[rand_top]["hex"]
        colors_to_match = None
        palettes_temp = copy.deepcopy(db.colors)
        while len(palettes_temp) > 0:
            #assume we always find color
            rand_palette = random.choice(palettes_temp)
            palettes_temp.remove(rand_palette)
            if top_hex in rand_palette:
                matched_colors = copy.deepcopy(rand_palette)
            if matched_colors != None:
                for bottom in _db.get_clothe_by_type("bottom"):
                    bottom_hex = _db.get_hex(bottom)
                    if (bottom_hex in matched_colors) and (bottom_hex != top_hex):
                        found = True
                        matched_bottom = bottom

   
    return {"top": _db.get_pic(matched_top), 
        "bottom": _db.get_pic(matched_bottom), 
        "colors": matched_colors}






