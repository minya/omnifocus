from model.context import Context
from model.folder import Folder
from model.task import Task
from model.xmlutil import extract_tag

__author__ = 'minya'

from xml.etree import ElementTree

def render_task(tree, t, prefix):
	if t.completed <> None:
		return
	print prefix + " " + t.name + " (" + (t.modified or "never") +  ")"
	if tree.has_key(t.id):
		for task in tree[t.id]:
			render_task(tree, task, prefix + '\t')

tree = ElementTree.parse("examples/contents.xml")
root = tree.getroot()
tasks = dict()
tasks_tree = dict()
folders = dict()
folders_tree = dict()
contexts = dict()
contexts_tree = dict()

for e in root:
	tag = extract_tag(e.tag)
	if tag == 'task':
		task = Task()
		task.fromXmlNode(e)
		tasks[task.id] = task
		parent = task.parentRef or "/"
		if not tasks_tree.has_key(parent):
			tasks_tree[parent] = []
		tasks_tree[parent].append(task)
	elif tag == 'folder':
		folder = Folder()
		folder.fromXmlNode(e)
		folders[folder.id] = folder
		parent_fldr = folder.parentRef or "/"
		if not folders_tree.has_key(parent_fldr):
			folders_tree[parent_fldr] = []
		folders_tree[parent_fldr].append(folder)
	elif tag == 'context':
		context = Context()
		context.fromXmlNode(e)
		contexts[context.id] = context
		parent_ctx = context.parentRef or "/"
		if not contexts_tree.has_key(parent_ctx):
			contexts_tree[parent_ctx] = []
		contexts_tree[parent_ctx].append(context)

print "tasks: %i" % len(tasks)
print "folders: %i" % len(folders)
print "contexts: %i" % len(contexts)

for f in folders:
	print "[%s]" % folders[f].name
for task in tasks_tree["/"]:
	render_task(tasks_tree, task, "")
