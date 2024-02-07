#---External---
from dateutil.relativedelta import relativedelta
#---Odoo---
from odoo import models, fields

class EstateProperty(models.Model):
    #---Methods---
    def _set_date_availability_default(self):
        return fields.Date.context_today(self) + relativedelta(months=3)
    #---Data---
    _name = "estate.property"
    _description = "Propriété de l'immobilier"

    name = fields.Char("Nom", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Code postal")
    date_availability = fields.Date("Date valables", copy=False, default=_set_date_availability_default)
    expected_price = fields.Float("Prix attendu", required=True)
    selling_price = fields.Float("Prix de vente", readonly=True, copy=False)
    bedrooms = fields.Integer("Chambres", default=2)
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
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )

    active = fields.Boolean("Actif", default=True)