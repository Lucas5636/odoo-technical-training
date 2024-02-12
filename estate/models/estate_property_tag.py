#---External---
#---Odoo---
from odoo import models, fields

class EstatePropertyTag(models.Model):
    #---Private ---
    _name = "estate.property.tag"
    _description = "Tag de propriété de l'immobilier"
    # ---SQL Constraints---
    _sql_constraints = [
        ("check_price", "CHECK(price > 0)",
         "Le prix de l'offre devrait être supérieur à 0"),
    ]
    # ---Methods---
    #---Data---
    name = fields.Char("nom", required=True)