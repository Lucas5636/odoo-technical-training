#---External---
#---Odoo---
from odoo import models
class EstateProperty(models.Model):
    # ---Private ---
    _inherit = "estate.property"

    def action_sold(self):
        print("Hello from action sold")
        return super().action_sold()