from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def default_get(self, _fields):
        result = super(ResPartner, self).default_get(_fields)
        result['type'] = 'contact'
        if 'user_id' not in result:
            result['user_id'] = self.env.user
        if 'ww_is_person' in self._context:
            result['is_company'] = False
        return result
