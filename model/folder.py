__author__ = 'minya'

from model.entity import Entity

class Folder(Entity):
	def fromXmlNode(self, elem):
		Entity.fromXmlNode(self, elem)
