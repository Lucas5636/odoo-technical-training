#---External---
#---Odoo---
from odoo import models, fields

class EstatePropertyType(models.Model):
    #---Private ---
    _name = "estate.property.type"
    _description = "Type de propriété de l'immobilier"
    _order = "name"
    # ---SQL Constraints---
    _sql_constraints = [
        ("check_name", "UNIQUE(name)",
         "Le type de propriété existe déjà"),
    ]
    # ---Methods---
    #---Data---
    name = fields.Char("Nom", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Propriétés")
