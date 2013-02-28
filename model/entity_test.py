from xml.etree import ElementTree
from model.task import Task

__author__ = 'minya'

import unittest


class MyTestCase(unittest.TestCase):
	def test_merge(self):
		tree = ElementTree.fromstring(
			'<omnifocus xmlns="http://www.omnigroup.com/namespace/OmniFocus/v1" app-id="com.omnigroup.OmniFocus.iPad" app-version="79.4.0.175422" os-name="iPhone OS" os-version="6.1" machine-model="iPad">' +
			'<task id="l5FczgWVl2S">' +
			'<task idref="gZW06uIszyr"/>' +
			'<added>2012-08-28T04:55:12.824Z</added>' +
			'<modified>2012-09-05T08:00:16.788Z</modified>' +
			'<name>Kill duplicates</name>' +
			'<rank>0</rank>' +
			'<order>parallel</order>' +
			'</task>' +
			'</omnifocus>')

		tree_upd = ElementTree.fromstring(
			'<omnifocus xmlns="http://www.omnigroup.com/namespace/OmniFocus/v1" app-id="com.omnigroup.OmniFocus.iPad" app-version="79.4.0.175422" os-name="iPhone OS" os-version="6.1" machine-model="iPad">' +
			'<task id="l5FczgWVl2S" op="update">' +
			'<task idref="gZW06uIszyr"/>' +
			'<added>2012-08-28T04:55:12.824Z</added>' +
			'<modified>2012-09-05T08:00:16.788Z</modified>' +
			'<name>Kill duplicates in bases</name>' +
			'<rank>0</rank>' +
			'<order>parallel</order>' +
			'</task>' +
			'</omnifocus>')

		task = Task()
		task.fromXmlNode(tree[0])
		task.merge(tree_upd[0])
		self.assertEquals(task.name, "Kill duplicates in bases")


if __name__ == '__main__':
	unittest.main()
