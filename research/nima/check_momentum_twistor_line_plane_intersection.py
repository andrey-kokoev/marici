#!/usr/bin/env python3
"""Exact Cramer/Schouten identity for the N2MHV intersection-twistor primitive."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
xs=map(s.Integer,(1,2,4,7,11));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
def br(*q):return s.det(s.Matrix.hstack(*(Z[i] if isinstance(i,int) else i for i in q)))
X12=Z[1]*br(2,3,4,5)+Z[2]*br(3,4,5,1)
X345=Z[3]*br(4,5,1,2)+Z[4]*br(5,1,2,3)+Z[5]*br(1,2,3,4)
difference=s.simplify(X12+X345)
checks={'two_cramer_presentations_projectively_equal':difference==s.zeros(4,1),'lies_on_line_12':br(Z[1],Z[2],X12,Z[3])==0 and br(Z[1],Z[2],X12,Z[4])==0,'lies_in_plane_345':br(X12,Z[3],Z[4],Z[5])==0,'nonzero_generic_intersection':X12!=s.zeros(4,1)}
out={'schema':'marici.nima.momentum-twistor-line-plane-intersection.v1','source':'arXiv:1212.5605 acquired TeX, Cramers_rule preceding Table g2n_yangian_invariants','object':'(12) intersect (345)','first_presentation':'Z1<2345>+Z2<3451>','second_presentation':'Z3<4512>+Z4<5123>+Z5<1234>','evaluated_vector':[str(x) for x in X12],'projective_relation':'first_presentation = - second_presentation','projective_relation_residual':[str(x) for x in difference],'checks':checks,'passed':all(checks.values()),'scope':'Exact generic-rational verification of the projective intersection primitive used in N2MHV five-bracket products.'}
p=ROOT/'research/nima/results/momentum-twistor-line-plane-intersection.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
