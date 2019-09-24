# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Verification',
    'summary': 'Verification Module used by CLVsol Solutions.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_global_log',
    ],
    'data': [
        'security/verification_security.xml',
        'security/ir.model.access.csv',
        'views/verification_outcome_view.xml',
        'views/verification_outcome_log_view.xml',
        'views/verification_template_view.xml',
        'views/verification_template_log_view.xml',
        'views/verification_schedule_view.xml',
        'views/verification_schedule_log_view.xml',
        'views/verification_batch_view.xml',
        'views/verification_batch_log_view.xml',
        'views/verification_batch_member_view.xml',
        'views/referenceable_model_view.xml',
        'data/verification_batch_member.xml',
        'wizard/verification_outcome_mass_edit_view.xml',
        'wizard/verification_template_mass_edit_view.xml',
        'wizard/verification_schedule_mass_edit_view.xml',
        'wizard/verification_schedule_exec_view.xml',
        # 'wizard/verification_batch_exec_view.xml',
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
