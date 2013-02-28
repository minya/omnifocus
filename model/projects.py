import os
from zipfile import ZipFile

__author__ = 'Mikhail Brel <minya.drel@gmail.com>'
from model.state import State
from xml.etree import ElementTree


def render_task(tree, t, prefix):
	# if t.completed is not None:
	# 	return
	print prefix + ' ' + t.name + ' (' + (t.modified or 'never') + ')'
	if t.id in tree:
		for task in tree[t.id]:
			render_task(tree, task, prefix + '\t')


def render_folder(state, f, prefix):
	print prefix + ' [' + f.name + ']'
	if f.id in state.folders_tree:
		for f1 in state.folders_tree[f.id]:
			render_folder(state, f1, prefix + '\t')
	if f.id in state.tasks_tree:
		for t1 in state.tasks_tree[f.id]:
			render_task(state.tasks_tree, t1, prefix + '\t')


def render_state(state):
	print "tasks: %i" % len(state.tasks)
	print "folders: %i" % len(state.folders)
	print "contexts: %i" % len(state.contexts)

	for f in state.folders_tree["/"]:
		render_folder(state, f, "")
	for task in state.tasks_tree["/"]:
		if task.folderRef == "/":
			render_task(state.tasks_tree, task, "")


def get_state():
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
	return  state

# render_state(get_state())

