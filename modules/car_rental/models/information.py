from odoo import api, fields, models


class CarInformation(models.Model):
    _name = "car.information"
    _description = "Car rental type"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    type = fields.Char(string='ประเภทรถ', required=True)
    name = fields.Char(string='ชื่อรถ', required=True)
    car_reg = fields.Char(string='เลขทะเบียน', required=True)