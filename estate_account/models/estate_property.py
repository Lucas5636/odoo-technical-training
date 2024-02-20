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
        for property in self:
            self.env["account.move"].create({
                "partner_id": property.buyer_id.id,
                "move_type": "out_invoice",
                }
            ),
        return super().action_sold()