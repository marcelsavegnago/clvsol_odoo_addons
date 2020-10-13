# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Address(models.Model):
    _inherit = 'clv.address'

    person_ids = fields.One2many(
        comodel_name='clv.person',
        inverse_name='ref_address_id',
        string='Persons'
    )
    count_persons = fields.Integer(
        string='Persons (count)',
        compute='_compute_count_persons',
        # store=True
    )

    # @api.depends('person_ids')
    def _compute_count_persons(self):
        for r in self:
            r.count_persons = len(r.person_ids)


class Person(models.Model):
    _inherit = 'clv.person'

    ref_address_is_unavailable = fields.Boolean(
        string='Address is unavailable',
        default=False,
    )
    ref_address_id = fields.Many2one(comodel_name='clv.address', string='Address', ondelete='restrict')
    ref_address_code = fields.Char(string='Address Code', related='ref_address_id.code', store=False)

    ref_address_phone = fields.Char(string='Address Phone', related='ref_address_id.phone')
    ref_address_mobile_phone = fields.Char(string='Address Mobile', related='ref_address_id.mobile')
    ref_address_email = fields.Char(string='Address Email', related='ref_address_id.email')

    ref_address_category_names = fields.Char(
        string='Address Category Names',
        related='ref_address_id.category_ids.name',
        store=True
    )
    ref_address_category_ids = fields.Many2many(
        comodel_name='clv.address.category',
        string='Address Categories',
        related='ref_address_id.category_ids'
    )

    # @api.multi
    def do_person_get_ref_address_data(self):

        for person in self:

            _logger.info(u'>>>>> %s', person.ref_address_id)

            if (person.ref_address_id.id is not False):

                data_values = {}

                if person.ref_address_id.id is not False:

                    data_values['ref_address_id'] = person.ref_address_id.id

                    data_values['street_name'] = person.ref_address_id.street_name
                    data_values['street_number'] = person.ref_address_id.street_number
                    data_values['street_number2'] = person.ref_address_id.street_number2
                    data_values['street2'] = person.ref_address_id.street2
                    data_values['zip'] = person.ref_address_id.zip
                    data_values['city'] = person.ref_address_id.city
                    data_values['city_id'] = person.ref_address_id.city_id.id
                    data_values['state_id'] = person.ref_address_id.state_id.id
                    data_values['country_id'] = person.ref_address_id.country_id.id
                    # data_values['phone'] = person.ref_address_id.phone
                    # data_values['mobile'] = person.ref_address_id.mobile

                _logger.info(u'>>>>>>>>>> %s', data_values)

                person.write(data_values)

        return True


class Person_2(models.Model):
    _inherit = 'clv.person'

    ref_address_state = fields.Selection(
        string='Address State',
        related='ref_address_id.state',
        store=False
    )
