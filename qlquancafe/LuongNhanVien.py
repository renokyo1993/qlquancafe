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

class luong_nhanvien(osv.osv):
    _name = 'luong.nhan.vien'
    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for luong in self.browse(cr, uid, ids, context=context):
            res[luong.id] = {
                'total': 0.0,
            }
            
            tong = (luong.tienluong * luong.hsl) + luong.tienthuong

            res[luong.id]['total'] = tong 
        return res
    _columns = {
        
        'nhanvien_id': fields.many2one('nhan.vien','Mã Nhân Viên', required = True),
        'thangbl': fields.integer('Tháng Bảng Lương', required = True),
         'nambl': fields.integer('Năm Bảng Lương', required = True),
         'thuongthang': fields.boolean('Thưởng Tháng'),
         'tienluong': fields.float('Tiền Lương'),
         'tienthuong': fields.float('Tiền Thưởng'),
         'hsl': fields.float('Hệ Số Lương'),
         'total': fields.function(_amount_all, string='Tổng cộng', multi='sums', help="The total amount."),
         
    }
    # hàm này dc định nghĩa để khi có thay đổi sẽ thay đổi theo
    def onchange_luong(self, cr, uid, ids, thuongthang, context=None):
        if not thuongthang:
            self.write(cr, uid, ids, {'tienthuong':0}) # UPDATE giá trị
            return {'value':{'tienthuong':0}}
        else: 
            return {'value':{}}
     
    def _check_company_id(self, cr, uid, ids, context=None):
        for luongnv in self.browse(cr, uid, ids, context=context):
            luongnv_ids = self.search(cr, uid, [('id','!=',luongnv.id),('nhanvien_id','=',luongnv.nhanvien_id.id), ('thangbl','=',luongnv.thangbl), ('nambl','=',luongnv.nambl)])
            if luongnv_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['nhanvien_id','thangbl', 'nambl']),
    ]
luong_nhanvien()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
