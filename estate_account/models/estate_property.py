#---External---
import logging
_logger = logging.getLogger(__name__)
#---Odoo---
from odoo import models
class EstateProperty(models.Model):
    # ---Private ---
    _inherit = "estate.property"

    def action_sold(self):
        _logger.info("Hello from inherited action sold")
        return super().action_sold()