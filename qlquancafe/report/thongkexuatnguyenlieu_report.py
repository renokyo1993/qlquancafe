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

from openerp import tools
from openerp.osv import fields, osv

class phieuxuatnl_report(osv.osv):
    _name = "phieuxuatnl.report"
    _description = "Sales Orders Statistics"
    _auto = False
   
    _columns = {
        'ngayxuat': fields.date('Ngày Xuất', readonly=True),
        'year': fields.char('Year', size=4, readonly=True),
        'month': fields.selection([('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'),
            ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'),
            ('10', 'October'), ('11', 'November'), ('12', 'December')], 'Month', readonly=True),
        'day': fields.char('Day', size=128, readonly=True),
        
         'phieuxuat_id': fields.many2one('phieu.xuat.nguyen.lieu','Mã Phiếu Xuất', readonly = True),
         'nguyenlieu_id': fields.many2one('nguyen.lieu','Mã Nguyên Liệu', readonly = True),
         'soluong': fields.integer('Số Lượng',readonly = True),
         'slnl': fields.integer('Số Lượng Nguyên Liệu Xuất',readonly = True),

    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'phieuxuatnl_report')
        cr.execute("""
            create or replace view phieuxuatnl_report as (
                select
                   min(ctxnl.id) as id,
                    ctxnl.phieuxuat_id as phieuxuat_id,
                    ctxnl.nguyenlieu_id as nguyenlieu_id,
                    ctxnl.soluong as soluong,
                    
                   

                    count(pxnl.id) as slnl,
                    
                    to_char(pxnl.ngayxuat, 'YYYY') as year,
                    to_char(pxnl.ngayxuat, 'MM') as month,
                    to_char(pxnl.ngayxuat, 'YYYY-MM-DD') as day
                    
                from
                    chi_tiet_xuat_nguyen_lieu ctxnl
                      join phieu_xuat_nguyen_lieu pxnl on (pxnl.id=ctxnl.phieuxuat_id) 
            
                group by
                    ctxnl.phieuxuat_id,
                    ctxnl.nguyenlieu_id,
                    
                    pxnl.ngayxuat,
                    ctxnl.soluong
    
            )
        """)
phieuxuatnl_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
