from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("New Module"),
			"items": [
				{
					"type": "doctype",
					"name": "Reg",
					"description": _("Support queries from customers."),
				}
			]
		}
	]
