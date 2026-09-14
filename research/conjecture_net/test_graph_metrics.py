from graph_metrics import *

def test_metrics_derived_and_percent():
 g=MetricGraph((MetricAction('a',requires=frozenset({'i'})),MetricAction('b',frozenset({'a'}),terminal=True)),frozenset({'i'}),(frozenset({'a','b'}),));m=g.metrics();assert m=={'active_action_count':2.,'frontier_width':1.,'interface_deficit':0.,'coherence_burden':1.,'formal_outcome_entropy_bits':4.,'minimum_declared_terminal_depth':2.}
 h=MetricGraph((replace(g.actions[0],status='resolved'),g.actions[1]),g.interfaces,g.coherence_constraints).metrics();assert percent_change(m,h)['minimum_declared_terminal_depth']==-50

def test_zero_base_and_validation():
 assert percent_change({'x':0.},{'x':1.})=={'x':None}
 try:MetricGraph((MetricAction('a',frozenset({'missing'})),)).metrics();assert False
 except ValueError:pass

if __name__=='__main__':test_metrics_derived_and_percent();test_zero_base_and_validation();print('PASS 2/2')
