# ---Odoo---
from odoo import models, fields
class EstatePropertyTag(models.Model):
    # ---Private---
    _name = "estate.property.tag"
    _description = "Tag de propriétés de l'immobiliers"
    _order = "name"
    # ---SQL Constraints---
    _sql_constraints = [
        ("check_name", "UNIQUE(name)",
         "Le tag existe déjà"),
    ]
    # ---Data---
    name = fields.Char("Nom", required=True)
    color = fields.Integer("Couleur")