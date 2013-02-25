__author__ = 'minya'

class Location(object):
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	@staticmethod
	def fromXmlNode(elem):
		latitude = elem.attrib['latitude']
		longitude = elem.attrib['longitude']
		return Location(latitude, longitude)
