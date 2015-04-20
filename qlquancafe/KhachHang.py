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

class khach_hang(osv.osv):
    _name = 'khach.hang'
    _columns = {
        
        'name': fields.char('Mã Khách Hàng', size=32, required = True),
         'ten': fields.char('Tên Khách Hàng', size=32),
        'diachi': fields.char('Địa Chỉ', size=32),
         'sodienthoai': fields.char('Số Điện Thoại'),
         
         
    }
    def _check_company_id(self, cr, uid, ids, context=None):
        for khachhang in self.browse(cr, uid, ids, context=context):
            khachhang_ids = self.search(cr, uid, [('id','!=',khachhang.id),('name','=',khachhang.name)])
            if khachhang_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['name']),
    ]
khach_hang()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
