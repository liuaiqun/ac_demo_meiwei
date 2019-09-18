# -*- coding: utf-8 -*-
from odoo import http

# class AcDemoMeiwei(http.Controller):
#     @http.route('/ac_demo_meiwei/ac_demo_meiwei/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ac_demo_meiwei/ac_demo_meiwei/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ac_demo_meiwei.listing', {
#             'root': '/ac_demo_meiwei/ac_demo_meiwei',
#             'objects': http.request.env['ac_demo_meiwei.ac_demo_meiwei'].search([]),
#         })

#     @http.route('/ac_demo_meiwei/ac_demo_meiwei/objects/<model("ac_demo_meiwei.ac_demo_meiwei"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ac_demo_meiwei.object', {
#             'object': obj
#         })