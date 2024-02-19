#---External---
#---Odoo---
from odoo import models
class EstateProperty(models.Model):
    # ---Private ---
    _inherit = "estate.property"

    def action_sold(self):
        return super().action_sold()