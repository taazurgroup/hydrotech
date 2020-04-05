# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters)
        return columns, data

def get_columns():
	return [
                _("Quotation") + ":Link/Quotation:100",
                _("Customer ID") + ":Link/Customer:100",
                _("Customer Name") + ":Link/Customer:130"
        ]
