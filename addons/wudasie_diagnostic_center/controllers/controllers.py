# -*- coding: utf-8 -*-
# from odoo import http


# class WudasieDiagnosticCenter(http.Controller):
#     @http.route('/wudasie_diagnostic_center/wudasie_diagnostic_center', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wudasie_diagnostic_center/wudasie_diagnostic_center/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('wudasie_diagnostic_center.listing', {
#             'root': '/wudasie_diagnostic_center/wudasie_diagnostic_center',
#             'objects': http.request.env['wudasie_diagnostic_center.wudasie_diagnostic_center'].search([]),
#         })

#     @http.route('/wudasie_diagnostic_center/wudasie_diagnostic_center/objects/<model("wudasie_diagnostic_center.wudasie_diagnostic_center"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wudasie_diagnostic_center.object', {
#             'object': obj
#         })

