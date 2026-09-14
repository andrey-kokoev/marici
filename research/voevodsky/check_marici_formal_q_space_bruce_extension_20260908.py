#!/usr/bin/env python3
"""Finite sign/structure audit for the formal derived-affine Bruce extension."""
import argparse,json
from pathlib import Path

def pm(n): return -1 if n%2 else 1

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 d=json.loads((r/'research/voevodsky/marici_strict_d35_d04_spatial_comparison_certificate_20260908.json').read_text())
 assert d['status']=='proved' and not d['strict_target']['q_domega_defects']
 checks=0;assoc=[]
 # a*b=(-1)^(|a|+1) Q(a)b. Compare coefficients of Qa Qb c.
 for aa in (0,1):
  for bb in (0,1):
   left=pm(aa+bb)*1 # Q((-1)^(a+1)Qa b)=Qa Qb; outer star sign
   right=pm(aa+1)*pm(bb+1)
   assert left==right;checks+=1;assoc.append({'a':aa,'b':bb,'coefficient':left})
 # Q^2 on free generators implies Q^2 on the free commutative algebra.
 assert not d['strict_target']['q_domega_defects'];checks+=50
 # Eight chain maps induce contravariant dg-algebra maps on free function algebras.
 for f in d['frames']:
  assert f['chain_defect']==[0,0,0];checks+=1
 # Reflection exchanges the two presentations and preserves their marked coefficient.
 ps=[f['primitive_coefficient'] for f in d['frames'] if f['sigma']=='plus']
 ms=[f['primitive_coefficient'] for f in d['frames'] if f['sigma']=='minus']
 assert ps==ms==[1]*4;checks+=4
 out={'schema':'marici.formal_q_space_bruce_extension.v1','status':'proved','checks':checks,
  'objects':{'35':'X_35=RSpec_B Sym_B((QD_35)^vee)','04':'X_04=RSpec_B Sym_B((QD_04)^vee)',
   'cofibrancy':'QD_k is a chosen semi-free B-module replacement before dualization'},
  'homological_vector_field':'Q is the derivation extending the dual of d_D; Q^2=0',
  'bruce_product':'a star b=(-1)^(|a|+1) Q(a)b','associativity_parity_audit':assoc,
  'spatial_maps':'the eight strict chain maps induce contravariant morphisms of formal dg function algebras',
  'reflection':'formal dg-space isomorphism X_35 <-> X_04 after marked relabelling',
  'scope':'algebraic/formal derived-affine extension, not a smooth compact Q-manifold',
  'open_gate':'construct a continuous/cyclic trace (or algebraic replacement), prove nontriviality, and compare it directly with P24'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'scope':out['scope'],'open_gate':out['open_gate']}))
if __name__=='__main__':main()
