from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Propriété de l'immobilier"

    name = fields.Char("Nom", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Code postal")
    date_availability = fields.Date("Date valables", copy=False)
    expected_price = fields.Float("Prix attendu", required=True)
    selling_price = fields.Float("Prix de vente", readonly=True, copy=False)
    bedrooms = fields.Integer("Chambres")
    living_area = fields.Integer("Salon")
    facades = fields.Integer("Façades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Jardin")
    garden_area = fields.Integer("Coin jardin")
    garden_orientation = fields.Selection([
                            ('N', 'Nord'),
                            ('S', 'Sud'),
                            ('E', 'Est'),
                            ('O', 'Ouest')
        ], string="Orientation du jardin")
