#---External---
from dateutil.relativedelta import relativedelta
#---Odoo---
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

class EstateProperty(models.Model):
    #---Private attributes---
    _name = "estate.property"
    _description = "Propriété de l'immobilier"
    #---SQL Constraints---
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)",
         "Le prix de vente devrait être supérieur à 0"),
        ("check_selling_price", "CHECK(selling_price >= 0)",
         "Le prix shouaité devrait être supérieur ou égal à 0"),
    ]
    # ---Methods---
    def _set_date_availability_default(self):
        return fields.Date.context_today(self) + relativedelta(months=3)
    # ---Data---
    name = fields.Char("Nom", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Code postal")
    date_availability = fields.Date("Date valables", copy=False, default=_set_date_availability_default)
    expected_price = fields.Float("Prix shouaité", required=True)
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

    #---Constraints and onchanges---
    @api.constrains("selling_price")
    def _check_selling_price(self):
        for property in self:
            if (not float_is_zero(property.selling_price, precision_rounding=0.01) and
                    float_compare(property.selling_price, property.expected_price * 0.9, precision_rounding=0.01) < 0):
                raise ValidationError("Le prix de vente ne peut pas être plus petit que 90% du prix shouaité")
    @api.onchange("garden")
    def _onchange_partner_id(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "N"
        else:
            self.garden_area = 0
            self.garden_orientation = False
    #---Action methods---
    def action_sold(self):
        if "canceled" in self.mapped("state"):
            raise UserError("Les offres annulées ne peuvent pas être vendue")
        return self.write({"state": "sold"})
    def action_cancel(self):
        if "sold" in self.mapped("state"):
            raise UserError("Les offres vendues ne peuvent pas être annulée")
        return self.write({"state": "canceled"})
