from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Test"),
			"items": [
				{
					"type": "doctype",
					"name": "tst",
					"description": _("Support queries from customers."),
				}
			]
		}
	]
