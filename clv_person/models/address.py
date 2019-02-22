# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Address(models.Model):
    _inherit = 'clv.address'

    person_ids = fields.One2many(
        comodel_name='clv.person',
        inverse_name='ref_address_id',
        string='Persons'
    )
    count_persons = fields.Integer(
        string='Persons (count)',
        # compute='_compute_count_persons',
        # store=True
    )

    # @api.depends('person_ids')
    # def _compute_count_persons(self):
    #     for r in self:
    #         r.count_persons = len(r.person_ids)


class Person(models.Model):
    _inherit = 'clv.person'

    ref_address_id = fields.Many2one(comodel_name='clv.address', string='Address', ondelete='restrict')
    ref_address_code = fields.Char(string='Address Code', related='ref_address_id.code', store=False)

    ref_address_phone = fields.Char(string='Address Phone', related='ref_address_id.phone')
    ref_address_mobile_phone = fields.Char(string='Address Mobile', related='ref_address_id.mobile')
    ref_address_email = fields.Char(string='Address Email', related='ref_address_id.email')

    ref_address_category_ids = fields.Char(
        string='Address Categories',
        related='ref_address_id.category_ids.name',
        store=True
    )
