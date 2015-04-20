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

# Mỗi ngày sẽ có 1 nguyên liệu khác nhau hoặc giống nhau.

class ton_kho(osv.osv):
    _name = 'ton.kho'
    
    
    
    _columns = {
        
        'nguyenlieu_id': fields.many2one('nguyen.lieu','Mã Nguyên Liệu', required = True),
         'thoigian': fields.date('Thời Gian ', required = True),
         'soluongtk': fields.integer('Số Lượng'),
        
    }
    
    
        
    def _check_company_id(self, cr, uid, ids, context=None):
        for tk in self.browse(cr, uid, ids, context=context):
            tk_ids = self.search(cr, uid, [('id','!=',tk.id),('nguyenlieu_id','=',tk.nguyenlieu_id.id), ('thoigian','=',tk.thoigian)])
            if tk_ids:  
                return False
        return True

    _constraints = [
        (_check_company_id, 'Trùng dữ liệu', ['thoigian','nguyenlieu_id'  ]),
    ]
ton_kho()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
