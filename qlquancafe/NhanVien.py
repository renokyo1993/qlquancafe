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

class nhan_vien(osv.osv):
    _name = 'nhan.vien'
    _columns = {
        'name': fields.char('Mã Nhân Viên', size=32, required = True),
         'ho': fields.char('Họ Nhân Viên', size=32),
        'ten': fields.char('Tên Nhân Viên', size=32),
        'cmnd': fields.char('Chứng Minh Nhân Dân'),
         'gioitinh': fields.selection([('nam', 'Nam'),('nu', 'Nữ')], 'Giới Tính'),
         'ngaysinh': fields.date("Ngày Sinh"),
         'quequan': fields.char('Quê Quán', size=32),
         'dienthoai':fields.char('Số Điện Thoại', size=32),
         'ngayvao': fields.date("Ngày Vào Làm Việc"),
    }
    def _check_company_id(self, cr, uid, ids, context=None):
        for nhanvien in self.browse(cr, uid, ids, context=context):
            nhanvien_ids = self.search(cr, uid, [('id','!=',nhanvien.id),('name','=',nhanvien.name)])
            if nhanvien_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['name']),
    ]
    
nhan_vien()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
