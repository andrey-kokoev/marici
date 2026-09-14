from composite_arrow_tests import ArrowPath,OUTCOMES
from path_polarity_constraints import *

def test_forced_possible_impossible():
 p=PolarityExistenceProblem((ArrowPath('p',('a','b')),),(PathPolarityConstraint('p','*+'),))
 assert p.analyze({'a':frozenset({'++'}),'b':frozenset({'++'})})['status']=='forced'
 assert p.analyze({'a':frozenset({'++'}),'b':frozenset({'++','+-'})})['status']=='possible'
 r=p.analyze({'a':frozenset({'++'}),'b':frozenset({'+-'})});assert r['status']=='impossible' and r['minimal_unsat_core']==['b']

def test_typing_impossible_and_wildcards():
 p=PolarityExistenceProblem((ArrowPath('p',('a','b')),),(PathPolarityConstraint('p','-*'),))
 assert p.analyze({'a':frozenset({'++'}),'b':frozenset({'-+'})})['status']=='typing-impossible'
 assert p.analyze({'a':frozenset({'-+'}),'b':frozenset({'++'})})['status']=='forced'

def test_coherent_alternative_paths():
 p=PolarityExistenceProblem((ArrowPath('u',('a',)),ArrowPath('l',('b',))),(PathPolarityConstraint('u','*+'),),True)
 r=p.analyze({'a':frozenset({'++'}),'b':OUTCOMES});assert r['status']=='forced' and r['satisfying_assignments']==1

if __name__=='__main__':test_forced_possible_impossible();test_typing_impossible_and_wildcards();test_coherent_alternative_paths();print('PASS 3/3')
