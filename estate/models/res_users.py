# ---Odoo---
from odoo import models, fields
class ResUsers(models.Model):
    # ---Private attributes---
    _inherit = "res.users"
    # ---Relations---
    property_ids = fields.One2many("estate.property", "user_id", string="Propirétés", index=True,
                                   domain=[("state", "in", ["new", "offer_received"])])