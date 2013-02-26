__author__ = 'Mikhail Brel <minya.drel@gmail.com>'


def extract_tag(str_tag):
	pos = str_tag.find('}')
	return str_tag[pos + 1:]


def extract_ns(str_tag):
	pos = str_tag.find('}')
	return str_tag[0:pos + 1]