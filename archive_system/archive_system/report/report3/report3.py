# Copyright (c) 2024, Shujaa_Aldeen_almarami and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	# if not filters: filters = {}

	columns, data = [], []
	column = get_columns()
	cs_data = get_cs_data(filters)
	if not cs_data:
		frappe.msgprint(_('No records found'))
		return column, cs_data
	data = []
	for d in cs_data:
		row = frappe.dict({
				'trader_name': d.trader_name,
				'branch_name': d.branch_name,
				
		})
		data.append(row)
	
	return columns, data

def get_columns():
	return [
		{
			'fieldname': 'trader_name',
			'label': ("اسم التاجر"),
			'fieldtype': 'Link',
			'options': 'Trader'
		},
		{
			"fieldname":"branch_name",
			"label": (" branch"),
			"fieldtype": "Data",
		},
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = 'Trader',
		fields = ['trader_name','branch_name'],
		filters = conditions,
		order_by = 'trader_name desc'
	)
	return data

def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
	return conditions
