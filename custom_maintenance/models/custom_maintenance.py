from odoo import models, fields, api

class CustomMaintenance(models.Model):

    #_name = 'custom_maintenance'
    _inherit = 'maintenance.equipment'

    image = fields.Binary("Image")
    image_small = fields.Binary("Small-sized image")
    image_medium = fields.Binary("Medium-sized image")

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(asset_asset, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(asset_asset, self).write(vals)
