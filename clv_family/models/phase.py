# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Phase(models.Model):
    _inherit = 'clv.phase'

    family_ids = fields.One2many(
        comodel_name='clv.family',
        inverse_name='phase_id',
        string='Families',
        readonly=True
    )
    count_families = fields.Integer(
        string='Families (count)',
        compute='_compute_family_ids_and_count',
    )

    def _compute_family_ids_and_count(self):
        for record in self:

            search_domain = [
                ('phase_id', '=', record.id),
            ]

            families = self.env['clv.family'].search(search_domain)

            record.count_families = len(families)
            record.family_ids = [(6, 0, families.ids)]


class Family(models.Model):
    _inherit = 'clv.family'

    phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Phase',
        ondelete='restrict'
    )
