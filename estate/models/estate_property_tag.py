#---External---
#---Odoo---
from odoo import models, fields

class EstatePropertyTag(models.Model):
    #---Private ---
    _name = "estate.property.tag"
    _description = "Tag de propriété de l'immobilier"
    # ---SQL Constraints---
    _sql_constraints = [
        ("check_name", "UNIQUE(name)",
         "Le tag existe déjà"),
    ]
    # ---Methods---
    #---Data---
    name = fields.Char("nom", required=True)