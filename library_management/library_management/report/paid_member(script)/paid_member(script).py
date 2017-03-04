# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
def execute(filters=None):
    columns, data = [], []
    return get_columns(),get_filter_data(filters)


def get_columns():
    return [
        _("Library Member")+":Link/Library Member:150",
        _("Library Member Name")+":Data:150",
        _("Email ID")+":Data:100",
        _("Phone")+":Data:100"
    ]

def get_filter_data(filters):
    new_condition = ''
    if filters.get('library_member'):
        new_condition += " and `tabLibrary Member`.name = '{}'".format(filters.get('library_member'))
    
    if filters.get('phone'):
        new_condition += " and `tabLibrary Member`.phone = '{}'".format(filters.get('phone'))
    
    sql = frappe.db.sql("""select `tabLibrary Member`.name, CONCAT(`tabLibrary Member`.first_name, ' ', `tabLibrary Member`.last_name)as full_name, `tabLibrary Member`.email_id, `tabLibrary Member`.phone  from `tabLibrary Membership` inner join `tabLibrary Member`
        where `tabLibrary Membership`.library_member = `tabLibrary Member`.name and `tabLibrary Membership`.paid='1' {} ORDER BY `tabLibrary Member`.name""".format(new_condition))
    return sql
    
