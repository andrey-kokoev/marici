from coherence_pyramid import *
from composite_arrow_tests import ArrowPath

def test_layers_and_query():
 arrows=(TypedArrow('a','A','B',2),TypedArrow('b','B','C',2),TypedArrow('c','A','C',1));paths=(ArrowPath('long',('a','b')),ArrowPath('short',('c',)))
 p=CoherencePyramid(arrows,paths,(CoherenceLayer('square',(('long','short'),),(PathPattern('long','*+'),)),));r=p.run();assert r['survivor_count']>0 and r['layers'][0]['marginal_pruning_percent']<0 and r['best_query']['bits_per_cost']==1.0

def test_rejects_object_type_mismatch():
 try:CoherencePyramid((TypedArrow('a','A','B',1),TypedArrow('b','C','D',1)),(ArrowPath('p',('a','b')),),()).validate();assert False
 except ValueError:pass

if __name__=='__main__':test_layers_and_query();test_rejects_object_type_mismatch();print('PASS 2/2')
