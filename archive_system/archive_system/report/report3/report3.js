// Copyright (c) 2024, Shujaa_Aldeen_almarami and contributors
// For license information, please see license.txt

frappe.query_reports["Report3"] = {
	"filters": [
		{
			"fieldname":"trader_name",
			"label": ("اسم التاجر"),
			"fieldtype": "Link",
			'options': 'Trader'
		},
		{
			"fieldname":"branch_name",
			"label": ("اسم التاجر"),
			"fieldtype": "Data",
		},
	]
};