from odoo import fields , models,api

class Dock(models.Model):
    _inherit = 'stock.picking.batch'
    print("====2")
    dock = fields.Many2one("stock.picking.batch",string = "Dock")
    vehicle = fields.Many2one("fleet.vehicle",string = "Vehicle")
    vehicle_category = fields.Many2one("fleet.vehicle.model.category",string = "Vehicle Category")

    @api.depends("move_line_ids", "vehicle_category")
    def _compute_weight(self):
        for record in self:
            total_weight = sum(move_line.product_id.weight * move_line.quantity for move_line in record.move_line_ids if move_line.product_id and move_line.product_id.weight)
            max_weight = record.vehicle_category.max_weight
            record.weight = (total_weight / max_weight)*100 if max_weight != 0 else 1000

class stockpicking(models.Model):
    _inherit = 'stock.picking'
    volume = fields.Float(string = "Volume" )