# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
frappe.ignor_remake = True
class Article(Document):
	def on_submit(self):
		if self.quantity:
			self.make_article();

	def validate(self):
		if frappe.ignor_remake:
			if self.name_series and not self.quantity:
				frappe.throw("Quantity field must be filluped");

	def autoname(self):

		self.name = make_autoname('{}.####'.format(self.name_series if self.name_series else self.article_name))


		
	def make_article(self):
		
		for x in range(int(self.quantity)-1):

			article=frappe.new_doc('Article')
			article.set('article_name',self.article_name)
			article.set('author',self.author)
			article.set('name_series',self.name_series)
			frappe.ignor_remake = False
			article.save()
			article.submit()
		self.quantity = ""

		
