
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'B95A62A4372D160AB2E84968CA8116F4'
    
_lr_action_items = {'ACTIONCALL':([1,],[3,]),'INTENTS':([0,],[1,]),'SET_DATA':([4,],[5,]),'INIT_INTENT':([3,],[4,]),'$end':([2,5,],[0,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'create_call':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> create_call","S'",1,None,None,None),
  ('create_call -> INTENTS ACTIONCALL INIT_INTENT SET_DATA','create_call',4,'p_Create_CALL','Analyzer.py',13),
]
