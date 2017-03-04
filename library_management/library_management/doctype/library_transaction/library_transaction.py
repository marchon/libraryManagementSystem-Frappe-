# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class LibraryTransaction(Document):
    def validate(self):
        last_transaction = frappe.get_all("Library Transaction",
            fields=["transaction_type", "transaction_date"],
            filters = {
                "article": self.article,
                "transaction_date": ("<=", self.transaction_date),
                "name": ("!=", self.name)
            })
	#frappe.throw(str(last_transaction))
        if self.transaction_type=="Issue":
            msg = _("Article {0} {1} has not been recorded as returned since {2}")
            if last_transaction and last_transaction[0].transaction_type=="Issue":
                frappe.throw(msg.format(self.article, self.article_name,
                    last_transaction[0].transaction_date))
        else:
            if not last_transaction or last_transaction[0].transaction_type!="Issue":
                frappe.throw(_("Cannot return article not issued"))

    def on_submit(self):
        article = frappe.get_doc("Article",self.article)
        if self.transaction_type == "Issue":
            article.status = "Return";
            article.save()
        elif self.transaction_type == "Return":
            article.status = "Issue";
            article.save()
        else: frappe.msgprint("Please select transaction type")
    