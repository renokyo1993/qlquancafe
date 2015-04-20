# -*- coding: utf-8 -*-
##############################################################################
#
#    HLVSolution, Open Source Management Solution
#
##############################################################################
import time
from openerp.report import report_sxw
from openerp import pooler
from openerp.osv import osv
from openerp.tools.translate import _
import random
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, float_compare
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Parser(report_sxw.rml_parse):
        
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context=context)
        pool = pooler.get_pool(self.cr.dbname)
        self.localcontext.update({
            'get_phieunhap':self.get_phieunhap,
            
        })
    def get_phieunhap(self):
        wizard_data = self.localcontext['data']['form']
        manguyenlieu = wizard_data['nguyenlieu_id']
        phieunhap_obj = self.pool.get('chitiet.nhap')
        phieunhap_ids = phieunhap_obj.search(self.cr, self.uid, [('nguyenlieu_id','=',manguyenlieu[0])])
        return phieunhap_obj.browse(self.cr, self.uid, phieunhap_ids)
    
