from odoo import fields, models, api


class stockpicking(models.Model):
    _inherit = "stock.picking"
    vehicle_category = fields.Many2one(
        "fleet.vehicle.model.category", string="Vehicle Category"
    )
    weight = fields.Float(string="Weight", compute="_compute_weight", store="True")
    volume = fields.Float(string="Volume", compute="_compute_volume", store="True")

    @api.depends("product_id", "product_id.weight", "move_line_ids.quantity")
    def _compute_weight(self):
        for record in self:
            compute_weight = 0
            for move in record.move_line_ids:
                compute_weight += move.product_id.weight * move.quantity
            record.weight = compute_weight

    @api.depends("product_id", "product_id.volume", "move_line_ids.quantity")
    def _compute_volume(self):
        for record in self:
            compute_volume = 0
            for move in record.move_line_ids:
                compute_volume += move.product_id.volume * move.quantity
            record.volume = compute_volume