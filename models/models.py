# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'visit'

    name = fields.Char(string='Descripcion')
    customer = fields.Char(string='cliente')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'Telefonico')], string = 'Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
