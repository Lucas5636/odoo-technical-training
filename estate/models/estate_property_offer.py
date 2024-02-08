#---External---
#---Odoo---
from odoo import models, fields

class EstatePropertyOffer(models.Model):
    #---Methods---
    #---Define model---
    _name = "estate.property.offer"
    _description = "Offre de propriété de l'immobilier"
    #---Data---
    name = fields.Char("Nom", required=True)