from odoo import models, fields
class Dock(models.Model):
    _name = "custom.dock"

    name = fields.Char(string="Dock")