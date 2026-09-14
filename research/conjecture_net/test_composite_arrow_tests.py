from composite_arrow_tests import *

def fixture():return CompositeArrowTest('square',(ArrowPath('upper',('a','b')),ArrowPath('lower',('c','d'))),{'a':2,'b':2,'c':2,'d':2},4)

def test_composition_and_joint_score():
 assert compose_word(('+-','-+'))=='++';t=fixture();assert t.cost_reduction_percent()==-50;assert t.information_per_cost()==2

def test_coherence_and_localization():
 t=fixture();assert t.evaluate({'a':'++'})['status']=='incomplete';good={'a':'++','b':'++','c':'+-','d':'-+'};assert t.evaluate(good)['status']=='pass';bad={**good,'d':'--'};r=t.evaluate(bad);assert r['status']=='fail' and len(r['suspect_arrows'])==4

def test_rejects_ill_typed_observation():
 try:fixture().evaluate({'a':'++','b':'-+','c':'++','d':'++'});assert False
 except ValueError:pass

if __name__=='__main__':test_composition_and_joint_score();test_coherence_and_localization();test_rejects_ill_typed_observation();print('PASS 3/3')
