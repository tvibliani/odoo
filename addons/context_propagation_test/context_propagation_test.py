# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

import random

random.seed()

class test_partners_wizard(osv.osv_memory):
    _name = "test.partners.wizard"
    _description = "Testing tree_but_open for context durability"
    _columns = {
    }
    _defaults = {
    }
    def test_partners_open_window(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        if context is None:
            context = {}
        result = mod_obj.get_object_reference(cr, uid, 'context_propagation_test', 'action_partners_game_tree_1')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        important_value = random.randint(1,100)
        print '[step1] IMPORTANT_VALUE: %s' %important_value # print the important_vaule...

        result['context'] = str({'important_value':important_value})
        return result

test_partners_wizard()

class test_partners_level_wizard(osv.osv_memory):
        _name = "test.partners.level.wizard"
        _description = "Move game to next level"
        _columns = {
        }
        _defaults = {
        }
        def next_level(self, cr, uid, ids, context=None):
            if context == None:
                context = {} 
            print '[step2] IMPORTANT_VALUE: %s' %context.get('important_value',False) # it prints: "[step2] IMPORTANT_VALUE: False", i.e. the important_value is lost for the moment. Any suggestions?
            # ....

test_partners_level_wizard()

#
# ....then Wizard3 and stuff like that
# 

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

