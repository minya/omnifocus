__author__ = 'Mikhail Brel <minya.drel@gmail.com>'
from model.location import Location
from model.entity import Entity


class Context(Entity):
	def fromXmlNode(self, elem):
		Entity.fromXmlNode(self, elem)

		location_el_list = elem.findall('.//' + self._ns + 'location')
		self.location = None
		if len(location_el_list) > 0:
			self.location = Location.fromXmlNode(location_el_list[0])