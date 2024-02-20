#---External---
import logging
_logger = logging.getLogger(__name__)
#---Odoo---
from odoo import models, Command
class EstateProperty(models.Model):
    # ---Private ---
    _inherit = "estate.property"

    def action_sold(self):
        _logger.info("Hello from inherited action sold")
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        for property in self:
            self.env["account.move"].create({
                "partner_id": property.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
                "invoice_line_ids": [
                    Command.create({
                            "name": property.name,
                            "quantity": 1.0,
                            "price_unit": property.selling_price * 0.6,
                    }),
                    Command.create({
                            "name": "Administrative fees",
                            "quantity": 1.0,
                            "price_unit": 100.0,
                    }),
                ],
            })
        return super().action_sold()