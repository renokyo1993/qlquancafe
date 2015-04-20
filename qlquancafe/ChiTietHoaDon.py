# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import addons
import logging
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools

_logger = logging.getLogger(__name__)

class chitiet_hoadon(osv.osv):
    _name = 'chi.tiet.hoa.don'
    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
#         cur_obj = self.pool.get('res.currency')
        res = {}
        for ctn in self.browse(cr, uid, ids, context=context):
            res[ctn.id] = {
                'tong': 0.0,
            }
            tong = ctn.soluong * ctn.dongia

            res[ctn.id]['tong'] = tong 
        return res
    
#     def _price_unit_default(self, cr, uid, context=None):
#         if context is None:
#             context = {}
#         if context.get('check_total', False):
#             t = context['check_total']
#             for l in context.get('invoice_line', {}):
#                 if isinstance(l, (list, tuple)) and len(l) >= 3 and l[2]:
#                     tax_obj = self.pool.get('account.tax')
#                     p = l[2].get('price_unit', 0) * (1-l[2].get('discount', 0)/100.0)
#                     t = t - (p * l[2].get('quantity'))
#                     taxes = l[2].get('invoice_line_tax_id')
#                     if len(taxes[0]) >= 3 and taxes[0][2]:
#                         taxes = tax_obj.browse(cr, uid, list(taxes[0][2]))
#                         for tax in tax_obj.compute_all(cr, uid, taxes, p,l[2].get('quantity'), l[2].get('product_id', False), context.get('partner_id', False))['taxes']:
#                             t = t - tax['amount']
#             return t
#         return 0


    _columns = {
        
        'hoadon_id': fields.many2one('hoa.don','Mã Hóa Đơn', required = True),
         'dodung_id': fields.many2one('do.dung','Mã Đồ Dùng', required = True),
        'soluong': fields.integer('Số Lượng'),
        'dongia': fields.float('Đơn Giá'),
#         'price_unit': fields.float('Unit Price', required=True, digits_compute= dp.get_precision('Product Price')),
         'tong': fields.function(_amount_all, string='Tổng cộng', multi='sums'),
    }
    
    def onchange_dongia(self, cr, uid, ids, dodung_id, context=None):
            dd = self.pool.get('do.dung').browse (cr, uid, dodung_id , context=context)
            return {'value':{'dongia':dd.dongia}}
    
    def _check_company_id(self, cr, uid, ids, context=None):
        for cthd in self.browse(cr, uid, ids, context=context):
            cthd_ids = self.search(cr, uid, [('id','!=',cthd.id),('hoadon_id','=',cthd.hoadon_id.id), ('dodung_id','=',cthd.dodung_id.id)])
            if cthd_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['hoadon_id','dodung_id']),
    ]
chitiet_hoadon()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
