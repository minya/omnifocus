from model.entity import Entity

__author__ = 'Mikhail Brel <minya.drel@gmail.com>'
from model.context import Context
from model.folder import Folder
from model.task import Task
from model.xmlutil import extract_tag


class State(object):
	def fromXml(self, tree):
		self._tree = tree
		root = tree
		self.tasks = dict()
		self.tasks_tree = dict()
		self.folders = dict()
		self.folders_tree = dict()
		self.contexts = dict()
		self.contexts_tree = dict()

		for e in root:
			tag = extract_tag(e.tag)
			if tag == 'task':
				task = Task()
				task.fromXmlNode(e)
				self.tasks[task.id] = task
				parent = task.parentRef or task.folderRef or "/"
				if not parent in self.tasks_tree:
					self.tasks_tree[parent] = []
				self.tasks_tree[parent].append(task)
			elif tag == 'folder':
				folder = Folder()
				folder.fromXmlNode(e)
				self.folders[folder.id] = folder
				parent_folder = folder.parentRef or "/"
				if not parent_folder in self.folders_tree:
					self.folders_tree[parent_folder] = []
				self.folders_tree[parent_folder].append(folder)
			elif tag == 'context':
				context = Context()
				context.fromXmlNode(e)
				self.contexts[context.id] = context
				parent_ctx = context.parentRef or "/"
				if not parent_ctx in self.contexts_tree:
					self.contexts_tree[parent_ctx] = []
				self.contexts_tree[parent_ctx].append(context)

	def search_same(self, element):
		result = self._tree.findall(element.tag + "[@id='" + element.attrib["id"] + "\']")
		if len(result) > 0:
			return result[0]
		else:
			return None

	def merge(self, tree):
		for element in tree:
			same = self.search_same(element)
			if same is None:
				self._tree.append(element)
			else:
				e = Entity()
				e.fromXmlNode(same)
				e.merge(element)
