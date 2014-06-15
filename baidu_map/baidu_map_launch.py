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
from osv import osv

class launch_baidu_map(osv.osv):

    _inherit = "res.partner"

    def open_baidu_map(self, cr, uid, ids, context=None):
        address_obj= self.pool.get('res.partner')
        partner = address_obj.browse(cr, uid, ids, context=context)[0]
        url="http://map.baidu.com/?newmap=1&ie=utf-8&s=s%26wd%3D"
        if partner.country_id:
            url+=partner.country_id.name.strip()
        if partner.state_id:
            url+=partner.state_id.name.strip()          
        if partner.city:
            url+=partner.city.strip()           
        if partner.street:
            url+=partner.street.strip()

        return {
        'type': 'ir.actions.act_url',
        'url':url,
        'target': 'new'
        }

launch_baidu_map()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

