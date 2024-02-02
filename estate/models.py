from odoo import models

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Propriété de l'immobilier"

    name = field.Char('Nom')
    description = field.Text('Description')
    postcode = field.Char('Code postal')
    date_availability = field.Date('Date valables')
    expected_price = field.Float('Prix attendu')
    selling_price = field.Float('Prix de vente')
    bedrooms = field.Integer('Chambres')
    living_area = field.Integer('Salon')
    facades = field.Integer('Façades')
    garage = field.Boolean('Garage')
    garden = field.Boolean('Jardin')
    garden_area = field.Integer('Coin jardin')
    garden_orientation = field.Selection('Orientation du jardin')
