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

class chitiet_nhap(osv.osv):
    _name = 'chitiet.nhap'
    
    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
#         cur_obj = self.pool.get('res.currency')
        res = {}
        for ctn in self.browse(cr, uid, ids, context=context):
            res[ctn.id] = {
                'tong': 0.0,
            }
            tong = ctn.slnhap * ctn.dongia

            res[ctn.id]['tong'] = tong 
        return res
    
    _columns = {
        'phieunhap_id': fields.many2one('phieu.nhap','Mã Phiếu Nhập', required = True),
         'nguyenlieu_id': fields.many2one('nguyen.lieu','Mã Nguyên Liệu', required = True),
         'slnhap': fields.integer('Số Lượng Nhập'),
          'dongia':fields.float('Đơn Giá'),
#         'dongia': fields.float('Đơn Giá', required=True, digits_compute= dp.get_precision('Đơn Giá'), readonly=True, states={'draft': [('readonly', False)]}),
         'tong': fields.function(_amount_all, string='Tổng cộng', multi='sums', help="The total amount."),
        
    }
#     def onchange_dongia(self, cr, uid, ids, context=None):
#         for nguyenlieu in self.browse(cr, uid, ids, context=context):
#                 return {'value':{'dongia':nguyenlieu.dongia}}
            
    def onchange_dongia(self, cr, uid, ids, nguyenlieu_id, context=None):
       
       
            nl = self.pool.get('nguyen.lieu').browse (cr, uid, nguyenlieu_id , context=context)
            return {'value':{'dongia':nl.dongia}}

            
       
    def _check_company_id(self, cr, uid, ids, context=None):
        for ctn in self.browse(cr, uid, ids, context=context):
            ctn_ids = self.search(cr, uid, [('id','!=',ctn.id),('phieunhap_id','=',ctn.phieunhap_id.id),('nguyenlieu_id','=',ctn.nguyenlieu_id.id)])
            if ctn_ids:  
                return False
        return True
 
    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['phieunhap_id', 'nguyenlieu_id']),
    ]
    
    
     
chitiet_nhap()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
