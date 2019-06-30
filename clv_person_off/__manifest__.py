# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Person (Off)',
    'summary': 'Person (Off) Module used by CLVsol Solutions.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_global_log',
        'clv_partner_entity',
        'clv_person',
    ],
    'data': [
        'security/person_off_security.xml',
        'security/ir.model.access.csv',
        'views/person_off_view.xml',
        'views/person_off_log_view.xml',
        'views/off_instance_view.xml',
        'views/person_off_marker_view.xml',
        'views/person_off_category_view.xml',
        'views/res_partner_view.xml',
        'views/global_tag_view.xml',
        'views/address_view.xml',
        'views/family_view.xml',
        'views/person_view.xml',
        'views/address_off_view.xml',
        'views/family_off_view.xml',
        'wizard/person_off_mass_edit_view.xml',
        'wizard/person_off_contact_information_updt_view.xml',
        'wizard/person_associate_to_person_off_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
