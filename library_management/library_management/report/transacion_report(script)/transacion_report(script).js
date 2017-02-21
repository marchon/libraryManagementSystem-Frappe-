// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Transacion Report(Script)"] = {
	"filters": [
		{
		    "fieldname":"library_member",
		    "label": __("Member"),
		    "fieldtype": "Link",
		    "options": "Library Member"
		},
		{
		    "fieldname":"transaction_date",
		    "label": __("Transaction date"),
		    "fieldtype": "Date"
		}
	]
}
