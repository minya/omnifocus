__author__ = 'Mikhail Brel <minya.drel@gmail.com>'

from model.xmlutil import extract_ns


class Project():
	def __init__(self, folderRef, status, lastReview, reviewInterval):
		self.folderRef = folderRef
		self.status = status
		self.lastReview = lastReview
		self.reviewInterval = reviewInterval

	@staticmethod
	def FromXmlElement(elem):
		ns = extract_ns(elem.tag)
		folder_el_list = elem.findall('.//' + ns + 'folder')
		folderRef = None
		if len(folder_el_list) > 0:
			folderRef = folder_el_list[0].attrib['idref']
		status_el_list = elem.findall('.//' + ns + 'status')
		status = None
		if len(status_el_list) > 0:
			status = status_el_list[0].text
		lastReview_el_list = elem.findall('.//' + ns + 'last-review')
		lastReview = None
		if len(lastReview_el_list) > 0:
			lastReview = lastReview_el_list[0].text
		reviewInterval_el_list = elem.findall('.//' + ns + 'review-interval')
		reviewInterval = None
		if len(reviewInterval_el_list) > 0:
			reviewInterval = reviewInterval_el_list[0].text
		return Project(folderRef, status, lastReview, reviewInterval)
