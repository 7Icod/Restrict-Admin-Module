# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.misc import groupby


class restrict_admin(models.Model):
    _name = 'restrict_admin'
    _description = 'restrict_admin.restrict_admin'

    name = fields.Char()
    value = fields.Boolean( ondelete='',string="Active", default=True)
    # value = fields.Selection([
    #     ('0','Disable'),
    #     ('1','Enable')
    # ])
    # rule = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
