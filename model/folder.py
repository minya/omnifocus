__author__ = 'Mikhail Brel <minya.drel@gmail.com>'

from model.entity import Entity


class Folder(Entity):
	def fromXmlNode(self, elem):
		Entity.fromXmlNode(self, elem)
