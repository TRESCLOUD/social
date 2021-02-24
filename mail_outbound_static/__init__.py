# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from . import models

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, pool):
    '''
    Desactiva todos los servidores de correos salientes y elimina las referencias de los servidores de correos
    salientes en las plantillas
    '''
    env = Environment(cr, SUPERUSER_ID, {})
    mail_server_ids = env['ir.mail_server'].search([])
    for mail_server in mail_server_ids:
        mail_server.active = False
        list_templates_ids = self.env['mail.template'].search([('mail_server_id', '=', mail_server.id)])
        if list_templates_ids:
            for template in list_templates_ids:
                template.mail_server_id = None
                    
