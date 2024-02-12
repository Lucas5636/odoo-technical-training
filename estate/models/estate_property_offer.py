#---External---
from dateutil.relativedelta import relativedelta
#---Odoo---
from odoo import models, fields, api
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    #---Private attributes---
    _name = "estate.property.offer"
    _description = "Offre de propriété de l'immobilier"
    #---SQL Constraints---
    _sql_constraints = [
        ("check_price", "CHECK(price > 0)",
         "Le prix de l'offre devrait être supérieur à 0"),
    ]
    # ---Methods---
    #---Data---
    price = fields.Float("Prix")
    status = fields.Selection(
            selection=[
                ("accepted", "Acceptée"),
                ("refused", "Refusée"),
            ],
        string="Status",
        copy=False,
        readonly=True,
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
    #---Action methods---
    def action_accept(self):
        if "refused" in self.mapped("property_id.offer_ids.status"):
            raise UserError("Vous ne pouvez pas accepté une offre déjà refusée")
        if "accepted" in self.mapped("property_id.offer_ids.status"):
            raise UserError("L'offre a déjà été acceptée")
        return self.mapped("property_id").write({"state": "offer_accepted", "selling_price": self.price,
                "buyer_id": self.partner_id.id,}) + self.write({"status": "accepted"})
    def action_refuse(self):
        if "accepted" in self.mapped("property_id.offer_ids.status"):
            raise UserError("Vous ne pouvez pas refusé une offre déjà acceptée")
        if "refused" in self.mapped("property_id.offer_ids.status"):
            raise UserError("L'offre a déjà été refusée")
        return self.write({"status": "refused"})