from odoo import models, fields

class Users(models.Model):
    _inherit = 'res.users'

    #--- Voir si déjà nécessaire car res.partner fonctionne sans fichier ---