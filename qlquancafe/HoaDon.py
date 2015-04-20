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

class hoa_don(osv.osv):
    _name = 'hoa.don'
    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
#         cur_obj = self.pool.get('res.currency')
        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = {
                 'amount_untaxed': 0.0,
#                 'amount_tax': 0.0,
#                'amount_total': 0.0,
            }
            val = val1 = 0.0
#             cur = order.order_line.id
            for line in order.order_line:
                val1 += line.tong
#                 val += self._amount_line_tax(cr, uid, line, context=context)
#             res[order.id]['amount_tax'] = cur_obj.round(cr, uid, cur, val)
            res[order.id]['amount_untaxed'] = val1
#             res[order.id]['amount_total'] = res[order.id]['amount_untaxed'] + res[order.id]['amount_tax']
        return res
    _columns = {
        
        'name': fields.char('Mã Hóa Đơn', size=32, required = True),
         'khachhang_id': fields.many2one('khach.hang','Mã Khách Hàng'),
        'ca_id': fields.many2one('ca.lam','Mã Ca'),
         'ngaylaphd': fields.date('Ngày Lập Hóa Đơn'),
         'order_line': fields.one2many('chi.tiet.hoa.don', 'hoadon_id', 'Order Lines'),
        'amount_untaxed':fields.function(_amount_all, string='Tổng cộng', multi='sums'),
    }
    def _check_company_id(self, cr, uid, ids, context=None):
        for hoadon in self.browse(cr, uid, ids, context=context):
            hoadon_ids = self.search(cr, uid, [('id','!=',hoadon.id),('name','=',hoadon.name)])
            if hoadon_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['name']),
    ]
hoa_don()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
