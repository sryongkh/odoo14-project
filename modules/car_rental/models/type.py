from odoo import  api, fields, models

class CarType(models.Model) :
    _name = "car.type"
    _description = "Information about type of car"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='ชื่อ', required=True)
    description = fields.Text(string='รายละเอียด', required=True)