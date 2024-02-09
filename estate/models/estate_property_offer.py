#---External---
#---Odoo---
from odoo import models, fields

class EstatePropertyOffer(models.Model):
    #---Methods---
    #---Define model---
    _name = "estate.property.offer"
    _description = "Offre de propriété de l'immobilier"
    #---Data---
    price = fields.Float("Prix")
    status = fields.Selection(
            selection=[
                ("accepted", "Acceptée"),
                ("refused", "Refusée"),
            ],
        string="Status",
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", string="Partenaire", required=True)
    property_id = fields.Many2one("estate.property", string="Propriété", required=True)