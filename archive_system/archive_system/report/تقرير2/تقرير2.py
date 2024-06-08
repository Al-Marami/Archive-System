# Copyright (c) 2024, Shujaa_Aldeen_almarami and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	if not filters: filters = {}

	columns, data = [], []
	column = get_columns()
	cs_data = get_cs_data(filters)
	if not cs_data:
		frappe.msgprint(_('No records found'))
		return column, cs_data
	data = []
	for d in cs_data:
		row = frappe._dict({
				'data_entary': d.data_entary,
				
		})
	data.append(row)
	return columns, data

def get_columns():
	return [
		{
			'fieldname': 'data_entary',
			'label': _("اسم التاجر"),
			'fieldtype': 'Data',
			'options': 'Treader'
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
		fields = ['data_entary'],
		filters = conditions,
		order_by = 'data_entary desc'
	)
	return data

def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
	return conditions