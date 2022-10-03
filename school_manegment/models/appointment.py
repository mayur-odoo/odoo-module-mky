# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields, api, _


class Appointment(models.Model):
    _name  = 'appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Appointment information"


    paitent_id = fields.Many2one('students', string="paitent")
    book_date  = fields.Date(string="Book Date") 
    paitent_age = fields.Integer(string="Paint-Age", compute="_compute_age")
    appointment_time = fields.Datetime(string="Appoitment time")
    paint_reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    paitnet_gender = fields.Selection([
            ("male", "Male"),
            ("female", "Female"), 
            ("other", "Other")],
            string="gender", default="male")

    
    @api.model
    def create(self, vals):
        if vals.get('paint_reference', _('New')) == _('New'):
            vals['paint_reference'] = self.env['ir.sequence'].next_by_code('appointment') or _('New')
        res = super(Appointment, self).create(vals)
        return res

    @api.onchange('paitent_id')
    def onchange_paitent_id(self):
        if self.paitent_id:
            if self.paitent_id.gender:
                self.paitnet_gender = self.paitent_id.gender
        else:
                self.paitnet_gender = ''

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.book_date is not False:
                rec.paitent_age = today.year - rec.book_date.year
            else:
                rec.book_date = 0
