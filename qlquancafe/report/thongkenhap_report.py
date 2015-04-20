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

class phieunhap_report(osv.osv):
    _name = "phieunhap.report"
    _description = "Sales Orders Statistics"
    _auto = False
   
    _columns = {
        'ngaynhap': fields.date('Ngày Nhập', readonly=True),
        'year': fields.char('Year', size=4, readonly=True),
        'month': fields.selection([('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'),
            ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'),
            ('10', 'October'), ('11', 'November'), ('12', 'December')], 'Month', readonly=True),
        'day': fields.char('Day', size=128, readonly=True),
        
         'phieunhap_id': fields.many2one('phieu.nhap','Mã Phiếu Nhập', readonly = True),
         'nguyenlieu_id': fields.many2one('nguyen.lieu','Mã Nguyên Liệu', readonly = True),
         'slnhap': fields.integer('Số Lượng',readonly = True),
         'slnl': fields.integer('Số Lượng Nguyên Liệu Nhập',readonly = True),
          'dongia':fields.float('Đơn Giá',readonly = True),
          'tong': fields.float('Tổng cộng', readonly = True),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'phieunhap_report')
        cr.execute("""
            create or replace view phieunhap_report as (
                select
                   min(ctn.id) as id,
                    ctn.phieunhap_id as phieunhap_id,
                    ctn.nguyenlieu_id as nguyenlieu_id,
                    ctn.slnhap as slnhap,
                    ctn.dongia as dongia,
                    sum(ctn.slnhap * ctn.dongia) as tong,

                    count(pn.id) as slnl,
                    
                    to_char(pn.ngaynhap, 'YYYY') as year,
                    to_char(pn.ngaynhap, 'MM') as month,
                    to_char(pn.ngaynhap, 'YYYY-MM-DD') as day
                    
                from
                    chitiet_nhap ctn
                      join phieu_nhap pn on (pn.id=ctn.phieunhap_id) 
            
                group by
                    ctn.phieunhap_id,
                    ctn.nguyenlieu_id,
                    
                    pn.ngaynhap,
                    ctn.slnhap,
                    ctn.dongia
            )
        """)
phieunhap_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
