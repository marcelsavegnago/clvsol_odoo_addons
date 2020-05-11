# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class PersonTag(models.Model):
    _description = 'Person Tag'
    _name = 'clv.person.tag'
    _inherit = 'clv.abstract.tag'

    code = fields.Char(string='Tag Code', required=False)

    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_tag_rel',
        column1='tag_id',
        column2='person_id',
        string='Persons'
    )


class Person(models.Model):
    _inherit = "clv.person"

    tag_ids = fields.Many2many(
        comodel_name='clv.person.tag',
        relation='clv_person_tag_rel',
        column1='person_id',
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