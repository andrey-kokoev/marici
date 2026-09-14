#!/usr/bin/env python3
"""Compute discriminant classes from incidences with the D4 exceptional curves."""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
R=Path(__file__).resolve().parents[3]
# central node first, then three outer nodes
C=s.Matrix([[2,-1,-1,-1],[-1,2,0,0],[-1,0,2,0],[-1,0,0,2]])
Ci=C.inv()
weights=[Ci[:,i] for i in range(4)]
# A weight is trivial mod root lattice iff all root-basis coordinates are integral.
def integral(v):return all(s.denom(x)==1 for x in v)
orders=[]
for w in weights:
 orders.append(next(k for k in range(1,5) if integral(k*w)))
nonzero_sums={}
for i in range(1,4):
 for j in range(i+1,4):
  # sum of two outer classes equals the third nonzero class
  nonzero_sums[f'w{i}+w{j}']=next(k for k in range(1,4) if integral(weights[i]+weights[j]-weights[k]))
checks={'central_weight_integral':integral(weights[0]),'central_class_zero':orders[0]==1,'outer_weights_half_integral':all(not integral(weights[i]) for i in range(1,4)),'outer_classes_order_two':orders[1:]==[2,2,2],'three_outer_classes_distinct':all(not integral(weights[i]-weights[j]) for i in range(1,4) for j in range(i+1,4)),'sum_rule':set(nonzero_sums.values())=={1,2,3},'smith_two_bits':[abs(int(smith_normal_form(C,domain=ZZ)[i,i])) for i in range(4)]==[1,1,2,2]}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.d4-thimble-incidence.v1','node_order':['central','outer_vector','outer_spinor','outer_conjugate_spinor'],'fundamental_weights_in_root_basis':[[str(x) for x in w] for w in weights],'orders_in_discriminant_group':orders,'criterion':{'central_incidence':'zero discriminant class','single_outer_incidence':'one of the three nonzero order-two classes'},'outer_sum_rule':nonzero_sums,'checks':checks,'passed':True,'geometric_gate':'To prove nonzero parity it is enough—and necessary in this plumbing frame—to show that the physical thimble meets an outer exceptional component rather than the central one.','next':'perform the first blowup of the physical branch of XY=E*q2 and record whether its strict transform lands on the central divisor or one of the three outer divisors'}
(R/'research/voevodsky/results/d4_thimble_incidence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'orders':orders,'criterion':out['criterion'],'gate':out['geometric_gate'],'next':out['next']}))
