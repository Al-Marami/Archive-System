// Copyright (c) 2024, Shujaa_Aldeen_almarami and contributors
// For license information, please see license.txt

frappe.query_reports["report_script"] = {
	"filters": [
		// {
		// 	"fieldname":"item_name",
		// 	"label": ("اسم المنتج"),
		// 	"fieldtype": "Link",
		// 	"options": "Trader Item"
		// },
		{
			"fieldname": "trader_name",
			"label": ("اسم التاجر"),
			"fieldtype": "Link",
			"options": "Trader",
			
		},
		{
			"fieldname": "price_type",
			"label": ("نوع العملة"),
			"fieldtype": "Select",
			"options": [
				"",
				{
					label: ("دولار امريكي"),
					value: "دولار امريكي",
				},
				{
					label: ("ريال سعودي"),
					value: "ريال سعودي",
				},
				{
					label: ("ريال يمني"),
					value: "ريال يمني",
				},
			],
			"default": "",

		},
		{
			"fieldname": "unique_number",
			"label": ("رقم الفاتورة"),
			"fieldtype": "Int",
			
		},
		
	]
	
};
