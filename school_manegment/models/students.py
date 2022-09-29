# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Student(models.Model):
    _name  = 'students'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "student information"

    name  = fields.Char(string="Name",required=True)
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    age  = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([
            ("male", "Male"),
            ("female", "Female"), 
            ("other", "Other")],
            string="gender", default="male")
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=True, default='draft')
    description = fields.Char(string="description")


    def action_button_sent(self):
        self.write({'state': "sent"})

    def action_button_confirm(self):
        self.write({'state': "sale"})

    def action_button_cancel(self):
        self.write({'state': "cancel"})


    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('students') or _('New')
        res = super(Student, self).create(vals)
        return res

