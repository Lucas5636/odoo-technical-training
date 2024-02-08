#---External---
#---Odoo---
from odoo import models, fields

class EstatePropertyTag(models.Model):
    #---Methods---
    #---Define model---
    _name = "estate.property.tag"
    _description = "Tag de propriété de l'immobilier"
    #---Data---
    name = fields.Char("nom", required=True)