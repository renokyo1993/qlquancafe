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

class phieu_nhap(osv.osv):
    _name = 'phieu.nhap'
    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):

        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = {
                 'amount_untaxed': 0.0,                
            }
            val = val1 = 0.0

            for line in order.chitiet_nhap:
                val1 += line.tong
              
            res[order.id]['amount_untaxed'] = val1         
        return res
    _columns = {
        
        'name': fields.char('Mã Phiếu Nhập', size=32, required = True),
         'nhanvien_id': fields.many2one('nhan.vien', 'Mã Nhân Viên'),
         'nhacungcap_id':fields.many2one('nha.cc', 'Mã Nhà Cung Cấp'),
        'ngaynhap': fields.date('Ngày Nhập'),
        'chitiet_nhap': fields.one2many('chitiet.nhap', 'phieunhap_id', 'Line'),
        'amount_untaxed':fields.function(_amount_all, string='Tổng cộng', 
#                                          
            multi='sums', help="The total amount."),
      
    }
    def _check_company_id(self, cr, uid, ids, context=None):
        for pn in self.browse(cr, uid, ids, context=context):
            pn_ids = self.search(cr, uid, [('id','!=',pn.id),('name','=',pn.name)])
            if pn_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['name']),
    ]
phieu_nhap()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
