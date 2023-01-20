from odoo import api, fields, models, _


class CarReservation(models.Model):
    _name = "car.reservation"
    _description = "Reservation car"

    reference = fields.Char(string='เลขที่จอง', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    car_type = fields.Char(string='ประเภทรถ', required=True)
    name = fields.Char(string='ชื่อรถ', required=True)
    car_reg = fields.Char(string='เลขทะเบียน', required=True)
    start_date = fields.Date(string='วันที่เริ่ม', required=True)
    end_date = fields.Date(string='วันที่คืน', required=True)

    @api.model
    def create(self, vals):
        if not vals.get('car_type') :
            vals['car_type'] = 'New Reservation'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('car.reservation') or _('New')
        res = super(CarReservation, self).create(vals)
        return res
