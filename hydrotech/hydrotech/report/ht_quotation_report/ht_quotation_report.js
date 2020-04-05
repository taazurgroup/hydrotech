// Copyright (c) 2016, Taazur and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["HT Quotation Report"] = {
	"filters": [

    {
    "fieldname":"from_date",
    "label" :("From Date"),
    "fieldtype":"Date",
    "default":frappe.datetime.month_start(date)
    },

    {
    "fieldname":"to_date",
    "label":("To Date"),
    "fieldtype":"Date",
    "default":get_today()
    }

	]
};
