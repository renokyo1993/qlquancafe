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

class hoadon_report(osv.osv):
    _name = "hoadon.report"
    _description = "Sales Orders Statistics"
    _auto = False
   
    _columns = {
        'ngaylaphd': fields.date('Ngày Nhập', readonly=True),
        'year': fields.char('Year', size=4, readonly=True),
        'month': fields.selection([('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'),
            ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'),
            ('10', 'October'), ('11', 'November'), ('12', 'December')], 'Month', readonly=True),
        'day': fields.char('Day', size=128, readonly=True),
        
         'hoadon_id': fields.many2one('hoa.don','Mã Hóa Đơn', readonly = True),
         'dodung_id': fields.many2one('do.dung','Mã Đồ Dùng', readonly = True),
         'soluong': fields.integer('Số Lượng ',readonly = True),
         'sldd': fields.integer('Số Lượng Đồ Dùng',readonly = True),
          'dongia':fields.float('Đơn Giá',readonly = True),
          'tong': fields.float('Tổng cộng', readonly = True),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'hoadon_report')
        cr.execute("""
            create or replace view hoadon_report as (
                select
                   min(cthd.id) as id,
                    cthd.hoadon_id as hoadon_id,
                    cthd.dodung_id as dodung_id,
                    cthd.soluong as soluong,
                    cthd.dongia as dongia,
                    sum(cthd.soluong * cthd.dongia) as tong,

                    count(hd.id) as sldd,
                    
                    to_char(hd.ngaylaphd, 'YYYY') as year,
                    to_char(hd.ngaylaphd, 'MM') as month,
                    to_char(hd.ngaylaphd, 'YYYY-MM-DD') as day
                    
                from
                    chi_tiet_hoa_don cthd
                      join hoa_don hd on (hd.id=cthd.hoadon_id) 
            
                group by
                    cthd.hoadon_id,
                    cthd.dodung_id,
                    
                    hd.ngaylaphd,
                    cthd.soluong,
                    cthd.dongia
            )
        """)
hoadon_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
