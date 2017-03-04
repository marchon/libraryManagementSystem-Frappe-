// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.query_reports["paid Member(Script)"] = {
	"filters": [
	{
		"fieldname":"library_member",
		"label":__("Member"),
		"fieldtype":"Link",
		"options": "Library Member"

	},
	{
		"fieldname":"phone",
		"label": __("Phone"),
		"fieldtype": "Data"
	}

	]
}
