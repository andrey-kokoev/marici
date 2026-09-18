#!/usr/bin/env python3
"""Selected exact component of the source phi N2MHV superinvariant."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_constructors import four_bracket as br,plane_plane_line_contraction as pp
from momentum_twistor_super import external_supertwistor,scale_supertwistor,super_line_plane_point,super_five_bracket,super_five_bracket_product_component
xs=map(s.Integer,(1,2,4,7,11,16,22,29,37));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
def evaluate(T):
 z={i:T[i].z for i in T};line=lambda a,b:pp(z[1],z[2],z[3],z[7],z[8],z[9],z[a],z[b])
 phi=s.factor(line(4,5)*line(4,6)/(br(z[1],z[2],z[3],z[4])*br(z[4],z[7],z[8],z[9])*line(5,6)))
 X45_789=super_line_plane_point(T[4],T[5],T[7],T[8],T[9]);X46_789=super_line_plane_point(T[4],T[6],T[7],T[8],T[9])
 X45_123=super_line_plane_point(T[4],T[5],T[1],T[2],T[3]);X46_123=super_line_plane_point(T[4],T[6],T[1],T[2],T[3])
 left=super_five_bracket((T[1],T[2],T[3],X45_789,X46_789));right=super_five_bracket((X45_123,X46_123,T[7],T[8],T[9]))
 pairs=((1,7),(2,8),(3,9),(1,7));return s.factor(phi*super_five_bracket_product_component(left,right,pairs)),phi
S={i:external_supertwistor(i,Z[i]) for i in Z};value,phi=evaluate(S);projective=[]
for i in range(1,10):
 T=dict(S);T[i]=scale_supertwistor(2,T[i]);projective.append(evaluate(T)[0]==value)
checks={'phi_nonzero':phi!=0,'selected_degree_eight_component_nonzero':value!=0,'projectively_invariant_all_nine_external_supertwistors':all(projective)}
out={'schema':'marici.nima.n2mhv-phi-composite-superinvariant.v1','source':'arXiv:1212.5605 Table g2n_yangian_invariants','formula':'phi [1,2,3,(45)cap(789),(46)cap(789)] [(45)cap(123),(46)cap(123),7,8,9]','component':'(chi_1 chi_7)^1 (chi_2 chi_8)^2 (chi_3 chi_9)^3 (chi_1 chi_7)^4','phi_value':str(phi),'component_value':str(value),'checks':checks,'passed':all(checks.values()),'scope':'One exact degree-eight component plus complete external projectivity check for the source phi-class N2MHV Yangian invariant.'}
p=ROOT/'research/nima/results/n2mhv-phi-composite-superinvariant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
