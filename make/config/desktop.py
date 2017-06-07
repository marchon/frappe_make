# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Make",
			"color": "blue",
			"icon": "octicon octicon-rocket",
			"type": "module",
			"label": _("Make")
		},
		{
			"module_name": "License",
			"color": "#B8860B",
			"icon": "fa fa-cloud",
			"type": "module",
			"label": _("License")
		}
	]
