class Clothe(object):

	def __init__(self, pic, color, clothe_type, season, clothe_id):
		self.pic = pic
		self.color = color
		self.type = clothe_type
		self.season = season
		self.id = clothe_id

	def make_dict(self):
		d = {
		    "pic": self.pic ,
		    "color": self.color ,
		    "type": self.type ,
		    "season": self.season , 
		    }
		    
		return self.id, d