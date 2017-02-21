# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.data import nowdate, getdate

class LibraryMembership(Document):
	def validate(self):
		self.update_member_status()


	def update_member_status(self):
		member = frappe.get_doc("Library Member", self.library_member)
		if getdate(self.to_date) < getdate(nowdate()):
			member.update_status('Inactive')
