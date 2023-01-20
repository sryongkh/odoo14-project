from odoo import api, fields, models


class CarInformation(models.Model):
    _name = "car.information"
    _description = "Car rental information"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char(string='ชื่อ', required=True)
    description = fields.Char(string='รายละเอียด')

