# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	return get_columns(), get_data(filters)

def get_columns():
	return [
		_("Library Member")+":Link/Library Member:100",
		_("Library Member Name")+":Data:100",
		_("Transaction Date")+":Date:100",
		_("Article Name")+":Data:100"
	]


def get_data(filters):
	conditions_and_value = ''

	if filters.get('library_member'):
		conditions_and_value +=" and library_member = '{}'".format(filters.get('library_member'))

	if filters.get('transaction_date'):
		conditions_and_value +=" and date(transaction_date) = date('{}')".format(filters.get('transaction_date'))

	sql = frappe.db.sql("""select library_member, member_name, transaction_date, article_name from `tabLibrary Transaction` 
		where name!='' {}""".format(conditions_and_value))
	# frappe.throw(str(sql))
	return sql
	# return frappe.get_all("Library Transaction", filters=filters, fields = ['library_member', 'member_name', 'transaction_date','article_name'], as_list=True)