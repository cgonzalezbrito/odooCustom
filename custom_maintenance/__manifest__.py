# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Custom Fields Maintenance',
    'version': '11.0.0.1',
    'description': """
        Add custom fields for maintenance addon
    """,
    'summary': """
        Add custom fields for maintenance addon
    """,
    'author': 'cgonzalezbrito',
    'license': 'AGPL-3',
    'category': 'Employes',
    'depends': [
        'maintenance',
        'hr_maintenance'
    ],
    'data': [
        'views/custom_maintenance.xml',
    ],
}
