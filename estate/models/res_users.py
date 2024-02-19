from odoo import models, fields

class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many("estate.property", "user_id", string="Propirétés", index=True,
                                   domain="[('state', '=', ('new', 'offer_received')]")