#---External---
from dateutil.relativedelta import relativedelta
#---Odoo---
from odoo import models, fields, api

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
    living_area = fields.Integer("Aire du salon")
    facades = fields.Integer("Façades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Jardin")
    garden_area = fields.Integer("Aire du jardin")
    garden_orientation = fields.Selection([
                            ('N', 'Nord'),
                            ('S', 'Sud'),
                            ('E', 'Est'),
                            ('O', 'Ouest')
        ], string="Orientation du jardin")
    state = fields.Selection(
        selection=[
            ("new", "Nouveau"),
            ("offer_received", "Offre Reçue"),
            ("offer_accepted", "Offre Acceptée"),
            ("sold", "Vendu"),
            ("canceled", "Annuler"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
    total_area = fields.Integer(string="Aire total", compute="_compute_total_area")
    best_price = fields.Float(string="Meilleur prix", compute="_compute_best_price")
    active = fields.Boolean("Actif", default=True)
    #---Relations---
    property_type_id = fields.Many2one("estate.property.type", string="Type de propriété")
    salesperson_id = fields.Many2one("res.users", string="Vendeurs", index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Acheteurs", index=True, copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offres")
    #---compute and search---
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for areas in self:
            areas.total_area = areas.living_area + areas.garden_area
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for prices in self:
            prices.best_price = max(prices.offer_ids.mapped("price")) if prices.offer_ids else 0.0
