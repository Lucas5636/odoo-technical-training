# ---Odoo---
from odoo import api, models, fields

class EstatePropertyType(models.Model):
    # ---Private---
    _name = "estate.property.type"
    _description = "Type de propriété de l'immobilier"
    _order = "sequence, name"
    # ---SQL Constraints---
    _sql_constraints = [
        ("check_name", "UNIQUE(name)",
         "Le type de propriété existe déjà"),
    ]
    # ---Data---
    name = fields.Char("Nom", required=True)
    sequence = fields.Integer("Séquence")
    offer_count = fields.Integer(string="Offres comptées", compute="_compute_offer_count")
    # ---Relations---
    property_ids = fields.One2many("estate.property", "property_type_id", string="Propriétés")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Offres")
    # ---Compute and Search---
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)