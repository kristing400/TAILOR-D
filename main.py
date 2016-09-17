from flask_api import FlaskAPI
import random
import copy

class Database(object):
    def __init__(self):
        self.db = dict() #store by id
        self.colors = dict() 
        self.lookup_table = {"f":dict(),
                             "m":dict(),
                            } #store by type

    def deleteAll(self):
        self.db = dict()

    def store_clothe(self, clothe_info):
        pic, color, color_hex, clothe_type, season, clothe_id, gender = clothe_info
        clothe_d = {
            "pic": pic ,
            "color": color ,
            "hex": color_hex,
            "type": clothe_type ,
            "season": season , 
            "gender": gender
            }
        self.db[clothe_id] =clothe_d
        if clothe_type not in self.lookup_table[gender]:
            self.lookup_table[gender][clothe_type] = [clothe_id]
        else:
            self.lookup_table[gender][clothe_type].append(clothe_id)

        return clothe_id

    def get_clothe_by_type(self , gender, choice):
        return self.lookup_table[gender][choice]

    def get_hex(self, clothe_id):
    	return self.db[clothe_id]["hex"]
    
    def get_pic(self, clothe_id):
    	return self.db[clothe_id]["pic"]

############Hardcoded stuff
app = FlaskAPI(__name__)
_db = Database()
clothes = [("f.222e59.png","blue","222e59","top","summer","01","f"),
           ("f.303633.png","black","303633","bottom","summer","02",'f'),
           ('f.333333.png','blue','333333','bottom','fall','03','f'),
           ('f.3c383d.png','black','3c383d','bottom','fall','04','f'),
           ('f.6b2737.png','red','6b2737','top','fall','05','f'),
           ('f.6d6d6d.png','gray','6d6d6d','top','summer','06','f'),
           ('f.90afaf.png','blue','90afaf','bottom','fall','07','f'),
           ('f.a05b33.png','orange','a05b33','top','summer','08','f'),
           ('f.2b526b.png','blue','2b526b','bottom','fall','09','f'),
           ('f.f4eod6.png','pink','f4eod6','top','summer','10','f'),
           ('f.f5e2c8.png', 'white','f5e2c8','bottom','summer','11','f'),
           ('f.fcf7f1.png','black','fcf7f1','bottom','fall','12','f'),
           ('f.fcfff5.png','white','fcfff5','top','summer','13','f'),
           ('f.ff6b6b.png','pink','ff6b6b','top','summer','14','f'),
           ('m.087e8b.png','blue','087e8b','bottom','summer','15','m'),
           ('m.0d5369.png','blue','0d5369','top','fall','16','m'),
           ('m.1e262b.png','black','1e262b','bottom','summer','17','m'),
           ('m.22333b.png','white','22333b','top','summer','18','m'),
           ('m.273b47.png','gray','273b47','top','summer','19','m'),
           ('m.2f4550.png','blue','2f4550','bottom','fall','20','m'),
           ('m.514e4e.png','gray','514e4e','top','summer','21','m'),
           ('m.545656.png','gray','545656','top','fall','22','m'),
           ('m.5e2222.png','red','5e2222','top','fall','23','m'),
           ('m.ce6659.png','orange','ce6659','bottom','summer','24','m'),
           ('m.f2cfa7.png','white','f2cfa7','bottom','fall','25','m'),
           ('m.f2f4f3.png','white','f2f4f3','bottom','fall','26','m'),
           ('m.fed766.png','yellow','fed766','top','summer','27','m'),
           ('m.fff2ee.png','white','fff2ee','bottom','fall','28','m'),
           ('f.212121.png', 'black', '212121', 'top','summer','29','f'),
           ('f.cea5c6.png','purple','cea5c6','top','summer','30','f'),
           ('f.c1302e.png','orange','c1302e','top','summer','31','f'),
           ('f.f2f7f2.png','white','f2f7f2','top','fall','32','f'),
           ('f.96e6b3.png','green','96e6b3','top','fall','33','f'),
           ('f.30262c.png','black','30262c','bottom','summer','34','f'),
           ('f.79b791.png','white','79b791','bottom','summer','35','f'),
           ('f.f67e7d.png','pink','f67e7d','bottom','summer','36','f'),
           ('f.757f60.png','green','757f60','bottom','summer','37','f'),
           ('f.0d1b1e.png','black','0d1b1e','bottom','summer','38','f'),
           ('m.414535.png', 'green', '414535', 'bottom', 'fall', '39', 'm'),
		   ('m.c2c5bb.png', 'white', 'c2c5bb', 'bottom', 'spring', '40', 'm'),
		   ('m.e0e0e0.png', 'white', 'e0e0e0', 'bottom', 'winter', '41', 'm'),
		   ('m.b4c4b6.png', 'blue', 'b4c4b6', 'bottom', 'spring', '42', 'm'),
		   ('m.140e14.png', 'blue', '140e14', 'bottom', 'fall', '43', 'm'),
		   ('m.d3532c.png', 'orange', 'd3532c', 'top', 'fall', '34', 'm'),
		   ('m.7a742e.png', 'brown', '7a742e', 'top', 'spring', '35', 'm'),
		   ('m.d6d093.png', 'white', 'd6d093', 'top', 'winter', '36', 'm'),
		   ('m.a50d08.png', 'red', 'a50d08', 'top', 'spring', '37', 'm'),
		   ('m.4b4c51.png', 'gray', '4b4c51', 'top', 'fall', '38', 'm')
          ]


palletes = [['0d5369','fff2ee'], ['414535','d6d093'],
            ['222e59','f5e2c8'], ['79b791','cea5c6'],
            ['22333b','f2f4f3'], ['7a742e','b4c4b6'],
            ['273b47','bfd7ea'], ['d3532c','c2c5bb'],
            ['2f4550','545656'], ['e0e0e0','4b4c51'],
            ['303633','6d6d6d'], ['140e14','a50d08'],
            ['333333','fcfff5'], ['0d1b1e','96e6b3'],
            ['514e4e','ce6659'],
            ['90afaf','a05b33'], ['ff6b6b','2b526b'],
            ['f2cfa7','5e2222'], ['fed766','1e262b'],
            ['f4e0d6','3c383d'], ['fcf7f1','6b2737']]

def store_clothes(clothes_list):
	for item in clothes_list:
		_db.store_clothe(item)


#############Initializing
store_clothes(clothes)
_db.colors = palletes


@app.route('/generate', methods=['GET'])
def generate():
    found = False
    matched_top = None
    matched_bottom = None
    matched_colors = None
    gender = random.choice(['f','m'])
    while not found:
        rand_top = random.choice(_db.get_clothe_by_type(gender,"top")) #returns id
        matched_top = rand_top
        top_hex = _db.db[rand_top]["hex"]
        colors_to_match = None
        palettes_temp = copy.deepcopy(_db.colors)
        while len(palettes_temp) > 0:
            #assume we always find color
            rand_palette = random.choice(palettes_temp)
            palettes_temp.remove(rand_palette)
            if top_hex in rand_palette:
                matched_colors = copy.deepcopy(rand_palette)
            if matched_colors != None:
                for bottom in _db.get_clothe_by_type(gender,"bottom"):
                    bottom_hex = _db.get_hex(bottom)
                    if (bottom_hex in matched_colors) and (bottom_hex != top_hex):
                        found = True
                        matched_bottom = bottom

   
    return {
    	"top": _db.get_pic(matched_top), 
        "bottom": _db.get_pic(matched_bottom), 
        "colors": '.'.join(matched_colors) + '.png'
        }



