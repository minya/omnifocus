__author__ = 'Mikhail Brel <minya.drel@gmail.com>'

from model.xmlutil import*


class Entity(object):
	def fromXmlNode(self, elem):
		entity_id = elem.attrib['id']
		ns = extract_ns(elem.tag)
		tag = extract_tag(elem.tag)
		parentRef_el_list = elem.findall('.//' + ns + tag)
		parentRef = None
		if len(parentRef_el_list) > 0:
			parentRef = parentRef_el_list[0].attrib['idref']
		added_el = elem.findall('.//' + ns + 'added')[0]
		added = added_el.text
		modified_el_list = elem.findall('.//' + ns + 'modified')
		if len(modified_el_list) > 0:
			modified = modified_el_list[0].text
		else:
			modified = None
		name_el = elem.findall('.//' + ns + 'name')[0]
		name = name_el.text
		rank_el = elem.findall('.//' + ns + 'rank')[0]
		rank = rank_el.text

		self._ns = ns
		self.id = entity_id
		self.parentRef = parentRef
		self.added = added
		self.modified = modified
		self.name = name
		self.rank = rank

	def toXmlNode(self, xmlNode):
		pass
