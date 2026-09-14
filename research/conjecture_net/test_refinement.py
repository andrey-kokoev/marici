from refinement import *

def plan():
 return RefinementPlan('global_gluing',(
  Gate('incidence',frozenset(),(InterfaceType('inc','axis','exceptional'),),1,3,2,2,True),
  Gate('multiplicity',frozenset({'inc'}),(InterfaceType('mult','incidence','Z'),),3,1,1),
  Gate('glue',frozenset({'mult'}),(InterfaceType('global','local collars','relative current'),),8,1,2),
 ),(('incidence','multiplicity'),('multiplicity','glue')))

def test_typed_ordering():
 p=plan();p.validate();assert p.next_gate(frozenset()).name=='incidence';assert p.next_gate(frozenset({'inc'}),frozenset({'incidence'})).name=='multiplicity'

def test_aggregation_is_not_premature():
 a=AggregationRule();children=('a','b');assert a.aggregate(children,{'a':'++'}) is None;assert a.aggregate(children,{'a':'++','b':'++'})=='++';assert a.aggregate(children,{'a':'++','b':'--'})=='--';assert a.aggregate(children,{'a':'-+'})=='-+'

def test_existential_terminal_aggregation():
 a=ExistentialAggregationRule();children=('x','y','z')
 assert a.aggregate(children,{'x':'+-'}) is None
 assert a.aggregate(children,{'x':'+-','y':'-+'})=='++'
 assert a.aggregate(children,{'x':'+-','y':'--','z':'--'})=='-+'

def test_rejects_type_alias_and_cycle():
 try:RefinementPlan('p',(Gate('a',frozenset(),(InterfaceType('x','A','B'),),1,1,1),Gate('b',frozenset(),(InterfaceType('x','C','D'),),1,1,1)),()).validate();assert False
 except ValueError:pass
 try:RefinementPlan('p',(Gate('a',frozenset(),(),1,1,1),Gate('b',frozenset(),(),1,1,1)),(('a','b'),('b','a'))).validate();assert False
 except ValueError:pass

if __name__=='__main__':test_typed_ordering();test_aggregation_is_not_premature();test_existential_terminal_aggregation();test_rejects_type_alias_and_cycle();print('PASS 4/4')
