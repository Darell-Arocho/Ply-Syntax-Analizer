
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'sASIG COMO DEFINA ELEMENTO_QUIMICO ENLACE FIN FIN_DE_LINEA IDENTIFICADOR INICIO LBRACK LPAREN OPERACION RBRACK RPAREN TIPO VALENCIAs : INICIO sentencias FINsentencias : sentencia FIN_DE_LINEA sentencias\n    | sentencia FIN_DE_LINEAsentencia : DEFINA IDENTIFICADOR COMO TIPO\n    | IDENTIFICADOR ASIG modelo_molecular\n    | OPERACION LPAREN IDENTIFICADOR RPARENmodelo_molecular : ELEMENTO_QUIMICO\n    | ELEMENTO_QUIMICO VALENCIA\n    | elemento grupo_funcional\n    | compuesto elemento\n    | compuesto elemento grupo_funcional\n    | compuesto compuesto compuestoscompuesto : ELEMENTO_QUIMICO\n    | ELEMENTO_QUIMICO VALENCIA\n    | elemento grupo_funcional\n    | elemento grupo_funcional ENLACE\n    | elemento ENLACEcompuestos : compuestos compuesto\n    | compuestoelemento : ELEMENTO_QUIMICO\n    | ELEMENTO_QUIMICO VALENCIAgrupo_funcional : grupo_funcional_inferior grupo_funcional_superior\n    | grupo_funcional_superior grupo_funcional_inferior\n    | LPAREN modelo_grupo_funcional RPAREN\n    | LBRACK modelo_grupo_funcional RBRACKgrupo_funcional_inferior : LBRACK modelo_grupo_funcional RBRACKgrupo_funcional_superior : LPAREN modelo_grupo_funcional RPARENmodelo_grupo_funcional : ENLACE modelo_molecular\n    | ELEMENTO_QUIMICO\n    | ELEMENTO_QUIMICO VALENCIA\n    | elemento grupo_funcional\n    | compuesto elemento\n    | compuesto elemento grupo_funcional\n    | compuesto compuesto compuestos'
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,8,],[0,-1,]),'DEFINA':([2,9,],[5,5,]),'IDENTIFICADOR':([2,5,9,12,],[6,10,6,19,]),'OPERACION':([2,9,],[7,7,]),'FIN':([3,9,13,],[8,-3,-2,]),'FIN_DE_LINEA':([4,15,16,20,21,22,23,29,30,31,32,33,35,43,44,45,47,48,51,57,58,59,60,61,62,],[9,-5,-7,-4,-8,-9,-17,-10,-20,-6,-16,-22,-23,-19,-12,-13,-11,-21,-24,-25,-18,-14,-15,-27,-26,]),'ASIG':([6,],[11,]),'LPAREN':([7,16,17,21,24,29,30,39,40,45,46,48,53,56,57,59,],[12,-20,26,-21,34,26,-20,-20,26,-20,26,-21,-21,26,-26,-21,]),'COMO':([10,],[14,]),'ELEMENTO_QUIMICO':([11,16,18,21,22,23,26,27,28,30,32,33,34,35,36,38,39,41,43,44,45,47,48,51,53,54,55,57,58,59,60,61,62,63,64,],[16,-13,30,-14,-15,-17,39,39,45,-13,-16,-22,39,-23,39,16,-13,30,-19,45,-13,-15,-14,-24,-14,-15,45,-25,-18,-14,-15,-27,-26,45,-15,]),'TIPO':([14,],[20,]),'RPAREN':([16,19,21,22,23,29,30,32,33,35,37,39,43,44,45,47,48,49,51,52,53,54,56,57,58,59,60,61,62,63,64,],[-7,31,-8,-9,-17,-10,-20,-16,-22,-23,51,-29,-19,-12,-13,-11,-21,61,-24,-28,-30,-31,-32,-25,-18,-14,-15,-27,-26,-34,-33,]),'RBRACK':([16,21,22,23,29,30,32,33,35,39,42,43,44,45,47,48,50,51,52,53,54,56,57,58,59,60,61,62,63,64,],[-7,-8,-9,-17,-10,-20,-16,-22,-23,-29,57,-19,-12,-13,-11,-21,62,-24,-28,-30,-31,-32,-25,-18,-14,-15,-27,-26,-34,-33,]),'VALENCIA':([16,30,39,45,],[21,48,53,59,]),'ENLACE':([16,17,21,22,26,27,29,30,33,34,35,36,39,40,45,46,47,48,51,53,54,56,57,59,60,61,62,64,],[-20,23,-21,32,38,38,23,-20,-22,38,-23,38,-20,23,-20,23,32,-21,-24,-21,32,23,-25,-21,32,-27,-26,32,]),'LBRACK':([16,17,21,25,29,30,39,40,45,46,48,51,53,56,59,],[-20,27,-21,36,27,-20,-20,27,-20,27,-21,-27,-21,27,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'sentencias':([2,9,],[3,13,]),'sentencia':([2,9,],[4,4,]),'modelo_molecular':([11,38,],[15,52,]),'elemento':([11,18,26,27,28,34,36,38,41,44,55,63,],[17,29,40,40,46,40,40,17,56,46,46,46,]),'compuesto':([11,18,26,27,28,34,36,38,41,44,55,63,],[18,28,41,41,43,41,41,18,55,58,43,58,]),'grupo_funcional':([17,29,40,46,56,],[22,47,54,60,64,]),'grupo_funcional_inferior':([17,25,29,40,46,56,],[24,35,24,24,24,24,]),'grupo_funcional_superior':([17,24,29,40,46,56,],[25,33,25,25,25,25,]),'modelo_grupo_funcional':([26,27,34,36,],[37,42,49,50,]),'compuestos':([28,55,],[44,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> INICIO sentencias FIN','s',3,'p_s','grammar.py',15),
  ('sentencias -> sentencia FIN_DE_LINEA sentencias','sentencias',3,'p_sentencias','grammar.py',19),
  ('sentencias -> sentencia FIN_DE_LINEA','sentencias',2,'p_sentencias','grammar.py',20),
  ('sentencia -> DEFINA IDENTIFICADOR COMO TIPO','sentencia',4,'p_sentencia','grammar.py',26),
  ('sentencia -> IDENTIFICADOR ASIG modelo_molecular','sentencia',3,'p_sentencia','grammar.py',27),
  ('sentencia -> OPERACION LPAREN IDENTIFICADOR RPAREN','sentencia',4,'p_sentencia','grammar.py',28),
  ('modelo_molecular -> ELEMENTO_QUIMICO','modelo_molecular',1,'p_modelo_molecular','grammar.py',32),
  ('modelo_molecular -> ELEMENTO_QUIMICO VALENCIA','modelo_molecular',2,'p_modelo_molecular','grammar.py',33),
  ('modelo_molecular -> elemento grupo_funcional','modelo_molecular',2,'p_modelo_molecular','grammar.py',34),
  ('modelo_molecular -> compuesto elemento','modelo_molecular',2,'p_modelo_molecular','grammar.py',35),
  ('modelo_molecular -> compuesto elemento grupo_funcional','modelo_molecular',3,'p_modelo_molecular','grammar.py',36),
  ('modelo_molecular -> compuesto compuesto compuestos','modelo_molecular',3,'p_modelo_molecular','grammar.py',37),
  ('compuesto -> ELEMENTO_QUIMICO','compuesto',1,'p_compuesto','grammar.py',41),
  ('compuesto -> ELEMENTO_QUIMICO VALENCIA','compuesto',2,'p_compuesto','grammar.py',42),
  ('compuesto -> elemento grupo_funcional','compuesto',2,'p_compuesto','grammar.py',43),
  ('compuesto -> elemento grupo_funcional ENLACE','compuesto',3,'p_compuesto','grammar.py',44),
  ('compuesto -> elemento ENLACE','compuesto',2,'p_compuesto','grammar.py',45),
  ('compuestos -> compuestos compuesto','compuestos',2,'p_compuestos','grammar.py',49),
  ('compuestos -> compuesto','compuestos',1,'p_compuestos','grammar.py',50),
  ('elemento -> ELEMENTO_QUIMICO','elemento',1,'p_elemento','grammar.py',54),
  ('elemento -> ELEMENTO_QUIMICO VALENCIA','elemento',2,'p_elemento','grammar.py',55),
  ('grupo_funcional -> grupo_funcional_inferior grupo_funcional_superior','grupo_funcional',2,'p_grupo_funcional','grammar.py',59),
  ('grupo_funcional -> grupo_funcional_superior grupo_funcional_inferior','grupo_funcional',2,'p_grupo_funcional','grammar.py',60),
  ('grupo_funcional -> LPAREN modelo_grupo_funcional RPAREN','grupo_funcional',3,'p_grupo_funcional','grammar.py',61),
  ('grupo_funcional -> LBRACK modelo_grupo_funcional RBRACK','grupo_funcional',3,'p_grupo_funcional','grammar.py',62),
  ('grupo_funcional_inferior -> LBRACK modelo_grupo_funcional RBRACK','grupo_funcional_inferior',3,'p_grupo_funcional_inferior','grammar.py',66),
  ('grupo_funcional_superior -> LPAREN modelo_grupo_funcional RPAREN','grupo_funcional_superior',3,'p_grupo_funcional_superior','grammar.py',70),
  ('modelo_grupo_funcional -> ENLACE modelo_molecular','modelo_grupo_funcional',2,'p_modelo_grupo_funcional','grammar.py',74),
  ('modelo_grupo_funcional -> ELEMENTO_QUIMICO','modelo_grupo_funcional',1,'p_modelo_grupo_funcional','grammar.py',75),
  ('modelo_grupo_funcional -> ELEMENTO_QUIMICO VALENCIA','modelo_grupo_funcional',2,'p_modelo_grupo_funcional','grammar.py',76),
  ('modelo_grupo_funcional -> elemento grupo_funcional','modelo_grupo_funcional',2,'p_modelo_grupo_funcional','grammar.py',77),
  ('modelo_grupo_funcional -> compuesto elemento','modelo_grupo_funcional',2,'p_modelo_grupo_funcional','grammar.py',78),
  ('modelo_grupo_funcional -> compuesto elemento grupo_funcional','modelo_grupo_funcional',3,'p_modelo_grupo_funcional','grammar.py',79),
  ('modelo_grupo_funcional -> compuesto compuesto compuestos','modelo_grupo_funcional',3,'p_modelo_grupo_funcional','grammar.py',80),
]
