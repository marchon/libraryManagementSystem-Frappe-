from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Main"),
			"items": [
				{
					"type": "doctype",
					"name": "New Accounts",
					"description": _("Support queries from customers."),
				}
			]
		}
	]
