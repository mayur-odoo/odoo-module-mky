# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOder(models.Model):
	_inherit = 'sale.order'


	student_reg_no =  fields.Many2one('students', string="Stundet")