#!/usr/bin/env python3
"""Exact check of a five-bracket with two constructed supertwistors."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_super import external_supertwistor,scale_supertwistor,super_line_plane_point,super_five_bracket
xs=map(s.Integer,(1,2,4,7,11,16,22,29));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
def build(T):
 X=super_line_plane_point(T[4],T[5],T[6],T[7],T[8])
 Y=super_line_plane_point(T[7],T[8],T[4],T[5],T[6])
 return X,Y,super_five_bracket((T[1],T[2],T[3],X,Y))
X,Y,value=build(S);projective=[]
for i in range(1,9):
 T=dict(S);T[i]=scale_supertwistor(2,T[i]);_,_,got=build(T)
 projective.append(got==value)
sample=(1,4,7,8);actual_support=set().union(*(set(m) for m in value))
checks={'first_intersection_support_45':set(X.chi)=={4,5},'second_intersection_support_78':set(Y.chi)=={7,8},'source_induced_seven_label_support':len(actual_support)==7,'degree_four':all(len(m)==4 for m in value),'expected_dense_support_size':len(value)==7**4,'generic_nonzero':value.get(sample,0)!=0,'projectively_invariant_all_external_supertwistors':all(projective)}
out={'schema':'marici.nima.double-composite-super-five-bracket.v1','source':'arXiv:1212.5605 Table g2n_yangian_invariants','formula':'[1,2,3,(45)cap(678),(456)cap(78)]','first_constructed_support':sorted(X.chi),'second_constructed_support':sorted(Y.chi),'effective_external_support':sorted(actual_support),'coefficient_count':len(value),'sample_component':'chi_1^1 chi_4^2 chi_7^3 chi_8^4','sample_value':str(value.get(sample,0)),'checks':checks,'passed':all(checks.values()),'scope':'Complete sparse degree-four evaluation at exact generic kinematics for a source bracket with two constructed supertwistors.'}
p=ROOT/'research/nima/results/double-composite-super-five-bracket.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
