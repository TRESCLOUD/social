# -*- coding: utf-8 -*-

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, pool):
    '''
    Desactiva todos los servidores de correos salientes
    '''
    env = Environment(cr, SUPERUSER_ID, {})
    mail_server_ids = env['ir.mail_server'].search([])
    for mail_server in mail_server_ids:
        mail_server.active = False