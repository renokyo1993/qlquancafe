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

class nguyen_lieu(osv.osv):
    _name = 'nguyen.lieu'
    
    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):

        res = {}
        
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = {
                 'amount_untaxed': 0,
                 'amount_untaxed1': 0,                
            }
            val = val1 = 0
            phuoc = phuoc1 = 0
            for line in order.order_line:
                val1 += line.soluongtk
            for line in order.order_line1:
                phuoc1 += line.soluong
            res[order.id]['amount_untaxed'] = val1 
            res[order.id]['amount_untaxed1'] = phuoc1  
            res[order.id]['amount_untaxed2'] = res[order.id]['amount_untaxed'] - res[order.id]['amount_untaxed1'] 
            if (res[order.id]['amount_untaxed2'] < 0):
                raise osv.except_osv(_('Warning!'),_('Số lượng xuất phải ít hơn số lượng tồn.')) 
        return res 
        
         
    _columns = {
        
        'name': fields.char('Mã Nguyên Liệu', size=32, required=True),
         'tennl': fields.char('Tên Nguyên Liệu', size=32),
         'donvitinh': fields.char('Đơn Vị Tính', size=32),
        'dongia': fields.float('Đơn Gía'),
        'order_line': fields.one2many('ton.kho', 'nguyenlieu_id', 'Order Lines'),
        'order_line1': fields.one2many('chi.tiet.xuat.nguyen.lieu', 'nguyenlieu_id', 'Order Lines'),
         'amount_untaxed':fields.function(_amount_all, string='Tổng Số Lượng Tồn Kho', multi='sums', help="The total amount.", readonly = True),
         'amount_untaxed1':fields.function(_amount_all, string='Tổng Số Lượng Xuất', multi='sums', help="The total amount.", readonly = True),
         'amount_untaxed2':fields.function(_amount_all, string='Số Lượng Tồn Kho (sau khi xuất)', multi='sums', help="The total amount."),
    }
    
    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        if context is None:
            context = {}
        if context.get('search_nguyenlieu'):
            
            sql = '''
                
                select nguyenlieu_id from ton_kho
                    
            '''
            cr.execute(sql)
            nguyen_lieu_ids = [row[0] for row in cr.fetchall()]
            args += [('id','in',nguyen_lieu_ids)]
        return super(nguyen_lieu, self).search(cr, uid, args, offset, limit, order, context, count)
    
    def name_search(self, cr, user, name, args=None, operator='ilike', context=None, limit=100):
        ids = self.search(cr, user, args, context=context, limit=limit)
        return self.name_get(cr, user, ids, context=context)
    
    def _check_company_id(self, cr, uid, ids, context=None):
        for nguyenlieu in self.browse(cr, uid, ids, context=context):
            nguyenlieu_ids = self.search(cr, uid, [('id','!=',nguyenlieu.id),('name','=',nguyenlieu.name)])
            if nguyenlieu_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['name']),
    ]
nguyen_lieu()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
