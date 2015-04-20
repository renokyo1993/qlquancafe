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

{
    'name': 'Quan Cafe',
    'version': '1.1',
    'category': 'QLQuanCafe',
    'sequence': 21,
    'website': '',
#     'summary': 'Jobs, Departments, Employees Details',
#     'description': """
# Human Resources Management
# ==========================
#  
# This application enables you to manage important aspects of your company's staff and other details such as their skills, contacts, working time...
#  
#  
# You can manage:
# ---------------
# * Employees and hierarchies : You can define your employee with User and display hierarchies
# * HR Departments
# * HR Jobs
#     """,
    'author': 'phamphuoc311093@gmail.com',
    'website': 'http://www.openerp.com',
#     'images': [
#         'images/hr_department.jpeg',
#         'images/hr_employee.jpeg',
#         'images/hr_job_position.jpeg',
#         'static/src/img/default_image.png',
#     ],
    'depends': ['report_aeroo','report_aeroo_ooo'],
    'data': [
        'security/quanly_security.xml',
        'security/ir.model.access.csv',
        'NhanVien_view.xml',
        'DoDung_view.xml',
        'NhaCungCap_view.xml',
         'PhieuNhap_view.xml',
        'ChiTietNhap_view.xml',
        'NguyenLieu_view.xml',
        'TonKho_view.xml',
        'KhachHang_view.xml',
        'Ca_view.xml',
        'HoaDon_view.xml',
        'ChiTietHoaDon_view.xml',
        'ChamCong_view.xml',
        'TonDoDung_view.xml',
        'PhieuXuatDoDung_view.xml',
        'PhieuXuatNguyenLieu_view.xml',
        'ChiTietXuatDoDung_view.xml',
        'ChiTietXuatNguyenLieu_view.xml',
        'LuongNhanVien_view.xml',
        
        'report/thongkenhap_report_view.xml',
        'report/thongkehoadon_report_view.xml',
        'report/thongkexuatnguyenlieu_report_view.xml',
        'report/thongkexuatdodung_report_view.xml',
        'report/phieunhap_report_view.xml',
        'report/print_nguyenlieu_view.xml',
        'wizard/print_nguyenlieu_view.xml',
        
        
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
