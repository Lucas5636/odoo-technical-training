#---External---
#---Odoo---
from odoo import models, fields

class EstatePropertyType(models.Model):
    #---Methods---
    #---Define model---
    _name = "estate.property.type"
    _description = "Type de propriété de l'immobilier"
    #---Data---
    name = fields.Char("Nom", required=True)