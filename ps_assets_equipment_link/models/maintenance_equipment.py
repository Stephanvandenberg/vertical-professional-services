# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    invoice_line_id = fields.Many2one(
        comodel_name="account.move.line",
        string="Origin line invoice",
    )
    asset_ids = fields.Many2many(
        comodel_name="account.asset",
        string="Assets",
    )
