import frappe
from frappe import throw
from frappe import msgprint, _
from frappe.utils import cint, flt

@frappe.whitelist(allow_guest=True)
def custom_autoname(self, method):
	from frappe.model.naming import getseries
	#Series for Seal Kit = SK, Series for Host Assembly = HA
	if self.ht_product_type == 'Seal Kit':
		self.name = 'SK' +"-"+ str(getseries('SK',5))
	if self.ht_product_type == 'Host Assembly':
		self.name = 'HA' +"-"+ str(getseries('HA',5))
