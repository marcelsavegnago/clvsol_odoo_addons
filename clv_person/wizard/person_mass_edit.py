# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

'''
Reference: http://help.openerp.com/question/18704/hide-menu-for-existing-group/

There are actually0-6 numbers for representing each job for a many2many/ one2many field

    (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
    (1, ID, { values }) -- update the linked record with id = ID (write values on it)
    (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the
               object completely, and the link to it as well)
    (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two
               objects but does not delete the target object itself)
    (4, ID) -- link to existing record with id = ID (adds a relationship)
    (5) -- unlink all (like using (3,ID) for all linked records)
    (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
'''

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonMassEdit(models.TransientModel):
    _description = 'Person Mass Edit'
    _name = 'clv.person.mass_edit'

    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_mass_edit_rel',
        string='Persons'
    )

    global_tag_ids = fields.Many2many(
        comodel_name='clv.global_tag',
        relation='clv_person_mass_edit_global_tag_rel',
        column1='person_id',
        column2='global_tag_id',
        string='Global Tags'
    )
    global_tag_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Global Tags:', default=False, readonly=False, required=False
    )

    category_ids = fields.Many2many(
        comodel_name='clv.person.category',
        relation='clv_person_mass_edit_category_rel',
        column1='person_id',
        column2='category_id',
        string='Categories'
    )
    category_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Categories:', default=False, readonly=False, required=False
    )

    marker_ids = fields.Many2many(
        comodel_name='clv.person.marker',
        relation='clv_person_mass_edit_marker_rel',
        column1='person_id',
        column2='marker_id',
        string='Markers'
    )
    marker_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Markers:', default=False, readonly=False, required=False
    )

    tag_ids = fields.Many2many(
        comodel_name='clv.person.tag',
        relation='clv_person_mass_edit_tag_rel',
        column1='person_id',
        column2='tag_id',
        string='Person Tag'
    )
    tag_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Person Tag:', default=False, readonly=False, required=False
    )

    partner_entity_code_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Partner Entity Code:', default=False, readonly=False, required=False
    )

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.model
    def default_get(self, field_names):

        defaults = super().default_get(field_names)

        defaults['person_ids'] = self.env.context['active_ids']

        return defaults

    @api.multi
    def do_person_mass_edit(self):
        self.ensure_one()

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            if self.global_tag_ids_selection == 'add':
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((4, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list
            if self.global_tag_ids_selection == 'remove_m2m':
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((3, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list
            if self.global_tag_ids_selection == 'set':
                m2m_list = []
                for global_tag_id in person.global_tag_ids:
                    m2m_list.append((3, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((4, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list

            if self.category_ids_selection == 'add':
                m2m_list = []
                for category_id in self.category_ids:
                    m2m_list.append((4, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list
            if self.category_ids_selection == 'remove_m2m':
                m2m_list = []
                for category_id in self.category_ids:
                    m2m_list.append((3, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list
            if self.category_ids_selection == 'set':
                m2m_list = []
                for category_id in person.category_ids:
                    m2m_list.append((3, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list
                m2m_list = []
                for category_id in self.category_ids:
                    m2m_list.append((4, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list

            if self.marker_ids_selection == 'add':
                m2m_list = []
                for marker_id in self.marker_ids:
                    m2m_list.append((4, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list
            if self.marker_ids_selection == 'remove_m2m':
                m2m_list = []
                for marker_id in self.marker_ids:
                    m2m_list.append((3, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list
            if self.marker_ids_selection == 'set':
                m2m_list = []
                for marker_id in person.marker_ids:
                    m2m_list.append((3, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list
                m2m_list = []
                for marker_id in self.marker_ids:
                    m2m_list.append((4, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list

            if self.tag_ids_selection == 'add':
                m2m_list = []
                for tag_id in self.tag_ids:
                    m2m_list.append((4, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list
            if self.tag_ids_selection == 'remove_m2m':
                m2m_list = []
                for tag_id in self.tag_ids:
                    m2m_list.append((3, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list
            if self.tag_ids_selection == 'set':
                m2m_list = []
                for tag_id in person.tag_ids:
                    m2m_list.append((3, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list
                m2m_list = []
                for tag_id in self.tag_ids:
                    m2m_list.append((4, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list

            if self.partner_entity_code_selection == 'set':
                if person.entity_code != person.code:
                    vals = {}
                    vals['entity_code'] = person.code
                    person.write(vals)
            if self.partner_entity_code_selection == 'remove':
                if person.entity_code is not False:
                    vals = {}
                    vals['entity_code'] = False
                    person.write(vals)

        return True
