# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AbstractFormat(models.AbstractModel):
    _description = 'Abstract Format'
    _name = 'clv.abstract.format'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    code = fields.Char(string='Code', required=False)
    description = fields.Char(string='Description')
    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=True)

    color = fields.Integer(string='Color Index')

    _sql_constraints = [
        ('code_uniq',
         'UNIQUE (code)',
         'Error! The Code must be unique!'),
        ('name_uniq',
         'UNIQUE (name)',
         'Error! The Name must be unique!'),
    ]
