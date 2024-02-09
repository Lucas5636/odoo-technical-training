#---External---
from dateutil.relativedelta import relativedelta
#---Odoo---
from odoo import models, fields, api

class EstatePropertyOffer(models.Model):
    #---Methods---
    #---Define model---
    _name = "estate.property.offer"
    _description = "Offre de propriété de l'immobilier"
    #---Data---
    price = fields.Float("Prix")
    status = fields.Selection(
            selection=[
                ("accepted", "Acceptée"),
                ("refused", "Refusée"),
            ],
        string="Status",
        copy=False,
    )
    validity = fields.Integer("Validité (jour(s))", default=7)
    date_deadline = fields.Date(string="Date limite", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    partner_id = fields.Many2one("res.partner", string="Partenaire", required=True)
    property_id = fields.Many2one("estate.property", string="Propriété", required=True)
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for dates in self:
            date = dates.create_date.date() if dates.create_date else fields.Date.today()
            dates.date_deadline = date + relativedelta(days=dates.validity)
    def _inverse_date_deadline(self):
        for dates in self:
            date = dates.create_date.date() if dates.create_date else fields.Date.today()
            dates.validity = (dates.date_deadline - date).days