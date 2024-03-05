from odoo import fields , models,api

class stockpicking(models.Model):
    _inherit = 'stock.picking'
    print("====2")
    vehicle_category = fields.Many2one("fleet.vehicle.model.category",string = "Vehicle Category")
    weight = fields.Float(string = "Weight", compute="_compute_weight",store="True")
    volume = fields.Float(string = "Volume", compute="_compute_volume",store="True")

    @api.depends("move_line_ids", "vehicle_category")
    def _compute_volume(self):
        for record in self:
            total_volume = sum(move_ids.product_id.volume * move_ids.quantity for move_ids in record.move_ids if move_ids.product_id and move_ids.product_id.volume)
            max_volume = record.vehicle_category.max_volume
            record.volume = (total_volume / max_volume)*100 if max_volume!= 0 else 100

    @api.depends("move_line_ids", "vehicle_category")
    def _compute_weight(self):
        for record in self:
            total_weight = sum(move_ids.product_id.weight * move_ids.quantity for move_ids in record.move_ids if move_ids.product_id and move_ids.product_id.weight)
            max_weight = record.vehicle_category.max_weight
            record.weight = (total_weight / max_weight)*100 if max_weight != 0 else 100



    