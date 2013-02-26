__author__ = 'Mikhail Brel <minya.drel@gmail.com>'

from model.entity import Entity
from model.project import Project


class Task(Entity):
	@staticmethod
	def get_string_field(elem, ns, elem_name):
		el_list = elem.findall('.//' + ns + elem_name)
		if len(el_list) > 0:
			return el_list[0].text
		else:
			return None

	def fromXmlNode(self, elem):
		Entity.fromXmlNode(self, elem)

		project_el_list = elem.findall('.//' + self._ns + 'project')
		project = None
		if len(project_el_list) > 0:
			project = Project.FromXmlElement(project_el_list[0])

		completed = Task.get_string_field(elem, self._ns, "completed")
		due = Task.get_string_field(elem, self._ns, "due")
		start = Task.get_string_field(elem, self._ns, "start")
		order = Task.get_string_field(elem, self._ns, "order")

		self.project = project
		self.completed = completed
		self.due = due
		self.start = start
		self.order = order or "parallel"
