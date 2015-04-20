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

class phieuxuatdd_report(osv.osv):
    _name = "phieuxuatdd.report"
    _description = "Sales Orders Statistics"
    _auto = False
   
    _columns = {
        'ngayxuat': fields.date('Ngày Xuất', readonly=True),
        'year': fields.char('Year', size=4, readonly=True),
        'month': fields.selection([('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'),
            ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'),
            ('10', 'October'), ('11', 'November'), ('12', 'December')], 'Month', readonly=True),
        'day': fields.char('Day', size=128, readonly=True),
        
         'phieuxuat_id': fields.many2one('phieu.xuat.do.dung','Mã Phiếu Xuất', readonly = True),
         'dodung_id': fields.many2one('do.dung','Mã Đồ Dùng', readonly = True),
         'slxuat': fields.integer('Số Lượng',readonly = True),
         'sldd': fields.integer('Số Lượng Đồ Dùng Xuất',readonly = True),

    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'phieuxuatdd_report')
        cr.execute("""
            create or replace view phieuxuatdd_report as (
                select
                   min(ctxdd.id) as id,
                    ctxdd.phieuxuat_id as phieuxuat_id,
                    ctxdd.dodung_id as dodung_id,
                    ctxdd.slxuat as slxuat,
                    
                   

                    count(pxdd.id) as sldd,
                    
                    to_char(pxdd.ngayxuat, 'YYYY') as year,
                    to_char(pxdd.ngayxuat, 'MM') as month,
                    to_char(pxdd.ngayxuat, 'YYYY-MM-DD') as day
                    
                from
                    chi_tiet_xuat_do_dung ctxdd
                      join phieu_xuat_do_dung pxdd on (pxdd.id=ctxdd.phieuxuat_id) 
            
                group by
                    ctxdd.phieuxuat_id,
                    ctxdd.dodung_id,
                    
                    pxdd.ngayxuat,
                    ctxdd.slxuat
    
            )
        """)
phieuxuatdd_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
