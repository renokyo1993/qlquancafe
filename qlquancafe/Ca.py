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

class ca_lam(osv.osv):
    _name = 'ca.lam'
    _columns = {
        
        'name': fields.char('Mã Ca', size=32, required = True),
 #        'thuca': fields.char('Thứ Ca', size=32),
        'tenca': fields.selection([('sang', 'Sáng'),('chieu', 'Chiều'),('toi', 'Tối')], 'Tên Ca'),
         'batdau': fields.float('Bắt Đầu'),
         'ketthuc': fields.float('Kết Thúc'),
         'luongca': fields.float('Lương Ca'),
    }
    def _check_company_id(self, cr, uid, ids, context=None):
        for ca in self.browse(cr, uid, ids, context=context):
            ca_ids = self.search(cr, uid, [('id','!=',ca.id),('name','=',ca.name)])
            if ca_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['name']),
    ]
ca_lam()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
