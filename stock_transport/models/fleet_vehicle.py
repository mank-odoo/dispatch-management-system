from odoo import models, fields


class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"
    print("====1")
    max_weight = fields.Float(string="Max Weight")
    max_volume = fields.Float(string="Max Volume")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}({record.max_weight},{record.max_volume})"


