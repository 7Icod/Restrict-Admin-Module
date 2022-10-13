# -*- coding: utf-8 -*-
# from odoo import http


# class RestrictAdmin(http.Controller):
#     @http.route('/restrict_admin/restrict_admin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restrict_admin/restrict_admin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('restrict_admin.listing', {
#             'root': '/restrict_admin/restrict_admin',
#             'objects': http.request.env['restrict_admin.restrict_admin'].search([]),
#         })

#     @http.route('/restrict_admin/restrict_admin/objects/<model("restrict_admin.restrict_admin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restrict_admin.object', {
#             'object': obj
#         })
