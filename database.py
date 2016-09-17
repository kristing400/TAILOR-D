from pymongo import MongoClient

class Database(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.app.closet

    def store_clothe(self, clothe_info):
    	pic, color, clothe_type, season, clothe_id = clothe_info
    	clothe_d = {
		    "pic": pic ,
		    "color": color ,
		    "type": clothe_type ,
		    "season": season , 
		    }
        result = self.db.insert_one({
            clothe_id: clothe_d
        })
        return result.inserted_id

    def get_clothe(self, category, choice):
        result = []
        cursor = self.db.find({category: choice})
        for clothe in cursor:
            print clothe
            result.append(clothe)
        return result


test = Database()
clothetest = ('01.png','white','shorts','summer','01')
test.store_clothe(clothetest)
test.get_clothe('color','white')