#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2
from model import projects

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def render_task(tree, t):
	# if t.completed is not None:
	# 	return
	str = '<div class="task"><div class="caption">' + t.name + '</div>'
	if t.id in tree:
		for task in tree[t.id]:
			str += render_task(tree, task)
	str += '</div>'
	return  str


def render_folder(state, f):
	str = '<table class="folder"><tr><td class="folder-caption">' + f.name + '</td></tr><tr><td class="content">'
	if f.id in state.folders_tree:
		for f1 in state.folders_tree[f.id]:
			str += render_folder(state, f1)
	if f.id in state.tasks_tree:
		for t1 in state.tasks_tree[f.id]:
			str += render_task(state.tasks_tree, t1)
	str += '</td></tr></table>'
	return str


def render_folders(state):
	str = ''
	for f in state.folders_tree["/"]:
		str += render_folder(state, f)
	return str


def render_tasks(state):
	str = ''
	for task in state.tasks_tree["/"]:
		if task.folderRef == "/":
			str += render_task(state.tasks_tree, task)
	return str


class MainHandler(webapp2.RequestHandler):
	def get(self):
		state = projects.get_state()
		res = ""
		res += render_folders(state)
		res += render_tasks(state)
		template_values = {
			'projects' : res
		}
		template = jinja_environment.get_template('main.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
