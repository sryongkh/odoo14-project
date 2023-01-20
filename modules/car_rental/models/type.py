from odoo import api, fields, models


class CarType(models.Model):
    _name = "car.type"
    _description = "Car rental type"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    type = fields.Char(string='ชื่อ', required=True)
    description = fields.Char(string='รายละเอียด')