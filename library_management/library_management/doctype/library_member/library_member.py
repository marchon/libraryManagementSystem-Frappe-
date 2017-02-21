# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from 	frappe.utils.data import nowdate, add_years

class LibraryMember(Document):
	def after_insert(self):
		self.make_membership()

	def make_membership(self):
		doc = frappe.new_doc("Library Membership")

		doc.set('library_member', self.name)
		doc.set('member_first_name', self.first_name)
		doc.set('member_last_name', self.last_name)
		doc.set('from_date', nowdate())
		doc.set('to_date', add_years(nowdate(), 1))
		doc.save()


	def update_status(self, status):
		self.status = status
		self.save()