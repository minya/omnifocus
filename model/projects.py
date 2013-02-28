import os
from zipfile import ZipFile

__author__ = 'Mikhail Brel <minya.drel@gmail.com>'
from model.state import State
from xml.etree import ElementTree


def render_task(tree, t, prefix):
	if t.completed is not None:
		return
	print prefix + ' ' + t.name + ' (' + (t.modified or 'never') + ')'
	if t.id in tree:
		for task in tree[t.id]:
			render_task(tree, task, prefix + '\t')

def render_state(state):
	print "tasks: %i" % len(state.tasks)
	print "folders: %i" % len(state.folders)
	print "contexts: %i" % len(state.contexts)

	for f in state.folders_tree["/"]:
		print "[%s]" % f.name
	for task in state.tasks_tree["/"]:
		render_task(state.tasks_tree, task, "")

state = State()
first = True
for file in os.listdir("examples"):
	if os.path.splitext(file)[1] != ".zip":
		continue
	zfile = ZipFile("examples/" + file)
	content = zfile.read("contents.xml")
	tree = ElementTree.fromstring(content)
	if first:
		state.fromXml(tree)
		first = False
	else:
		state.merge(tree)
	a = ""


# tree = ElementTree.parse("examples/contents.xml")
# state = State()
# state.fromXml(tree)
#
render_state(state)
#
# tree_update = ElementTree.parse("examples/contents_1.xml")
# state.merge(tree_update)
#
# render_state(state)
