# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PersonTag(models.Model):
    _inherit = 'clv.person.tag'

    person_history_ids = fields.Many2many(
        comodel_name='clv.person.history',
        relation='clv_person_history_tag_rel',
        column1='tag_id',
        column2='person_history_id',
        string='Persons (History)'
    )


class PersonHistory(models.Model):
    _inherit = "clv.person.history"

    tag_ids = fields.Many2many(
        comodel_name='clv.person.tag',
        relation='clv_person_history_tag_rel',
        column1='person_history_id',
        column2='tag_id',
        string='Person Tags'
    )
    tag_names = fields.Char(
        string='Tag Names',
        compute='_compute_tag_names',
        store=True
    )

    @api.depends('tag_ids')
    def _compute_tag_names(self):
        for r in self:
            tag_names = False
            for tag in r.tag_ids:
                if tag_names is False:
                    tag_names = tag.name
                else:
                    tag_names = tag_names + ', ' + tag.name
            r.tag_names = tag_names
