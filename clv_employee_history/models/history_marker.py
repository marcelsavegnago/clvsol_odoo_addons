# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields


class HistoryMarker(models.Model):
    _inherit = 'clv.history_marker'

    employee_ids = fields.One2many(
        comodel_name='hr.employee',
        inverse_name='history_marker_id',
        string='Employess',
        readonly=True
    )


class Employee(models.Model):
    _inherit = 'hr.employee'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )


class DepartmentHistory(models.Model):
    _inherit = 'hr.department.history'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )


class JobHistory(models.Model):
    _inherit = 'hr.job.history'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )


class EmployeeHistory(models.Model):
    _inherit = 'hr.employee.history'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )
