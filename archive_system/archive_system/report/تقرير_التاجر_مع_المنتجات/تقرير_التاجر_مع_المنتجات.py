# Copyright (c) 2024, Shujaa_Aldeen_almarami and contributors
# For license information, please see license.txt

import frappe
from frappe import _, _dict

def execute(filters=None):
	# columns, data = [], []
	# return columns, data
	if not filters: filters = {}

	data,columns = [], []
	columns = get_columns()
	cs_data = get_cs_data(filters)
	#if not cs_data:
	#	frappe.msgprint(_('No records found'))
	#	return columns, cs_data
	data = []
	for d in cs_data:
		row = frappe._dict({
			'item_name': d.item_name,
				'trader_name': d.trader_name,
				'pro_type': d.pro_type,
				'pro_country': d.pro_country,
				'unique_number': d.unique_number,
				'uom_type': d.uom_type,
				'uom': d.uom,
				'price_type': d.price_type,
				'rate': d.rate,
				'price_type1': d.price_type1,
				'rate1': d.rate1,
				'total1': d.total1,
				'total2': d.total2,
				'itme': d.itme,
		})
		data.append(row)
	
	return columns, data

def get_columns():
	return [
		
		{
			"fieldname":"trader_name",
			"label": _("اسم التاجر"),
			"fieldtype": "Link",
			"options": "Trader",
			'width': '120px'
		},
		{
			"fieldname":"item_name",
			"label": _("اسم المنتج"),
			"fieldtype": "Data",
			'width': '120px'
		},
		{
			"fieldname":"unique_number",
			"label": _("رقم الفاتورة"),
			"fieldtype": "Int",
			'width': '90px'
		},
		{
			"fieldname":"pro_type",
			"label": _("نوع المنتج"),
			"fieldtype": "Data",
			'width': '120px'
		},
		{
			"fieldname":"uom_type",
			"label": _("وحدة القياس"),
			"fieldtype": "Data",
			'width': '120px'
		},
		{
			"fieldname":"uom",
			"label": _("الكمية"),
			"fieldtype": "Data",
			'width': '50px'
		},
		{
			"fieldname":"price_type",
			"label": _("نوع العملة"),
			'width': '120px',
			
		},
		{
			"fieldname":"rate",
			"label": _("السعر"),
			"fieldtype": "Data",
			'width': '75px',
			
		},
		{
			"fieldname":"price_type1",
			"label": _("نوع العملة(مناقصة)"),
			'width': '120px'
		},
		{
			"fieldname":"rate1",
			"label": _("السعر (مناقصة)"),
			"fieldtype": "Data",
			'width': '50px'
		},
		{
			"fieldname":"total1",
			"label": _("السعر الاجمالي"),
			"fieldtype": "Data",
			'width': '120px'
		},
		{
			"fieldname":"total2",
			"label": _("السعر الاجمالي(مناقصة)"),
			"fieldtype": "Data",
			'width': '100px'
		},
		{
			"fieldname":"itme",
			"label": _("ملاحظة"),
			"fieldtype": "Text Editor",
			'width': '120px'
		},
	]
	
def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = 'Trader Item',
		fields = [
				'item_name','trader_name','pro_type','pro_country','price_type','rate','uom','uom_type','unique_number','price_type1','rate1','total2','total1','itme'
				],
		filters = conditions,
		order_by = 'item_name desc'
	)
	return data

def get_conditions(filters):
	conditions = {}
	
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
	
	
	return conditions

