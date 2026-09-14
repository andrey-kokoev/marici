#!/usr/bin/env python3
"""Compute the primitive A1^3 closure of four bitangent component differences."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
# Basis d1,d2,d3; d4=-(d1+d2+d3). Geometric intersections:
# di^2=-6 and di.dj=2 for i!=j.
G=s.Matrix([[-6,2,2],[2,-6,2],[2,2,-6]])
d1=s.Matrix([1,0,0]);d2=s.Matrix([0,1,0]);d3=s.Matrix([0,0,1]);d4=-(d1+d2+d3)
# Pairwise half-sums involving d1.
a12=(d1+d2)/2;a13=(d1+d3)/2;a14=(d1+d4)/2
A=s.Matrix.hstack(a12,a13,a14)
GA=s.simplify(A.T*G*A)
# Express the four component differences in the primitive alpha frame.
coords=[A.inv()*d for d in [d1,d2,d3,d4]]
checks={'difference_gram_rank_three':G.rank()==3,'fourth_square_minus_six':(d4.T*G*d4)[0]==-6,'fourth_pairings_two':all((d4.T*G*d)[0]==2 for d in [d1,d2,d3]),'half_sum_gram_A1_cubed':GA==-2*s.eye(3),'difference_sublattice_index_four':abs(int(s.Matrix.hstack(*coords[:3]).det()))==4,'all_difference_coordinates_odd':all(all(int(v)%2 for v in c) for c in coords),'four_distinct_mod_sign':len({tuple(map(int,c)) for c in coords})==4}
assert all(checks.values()),checks
mat=lambda M:[[int(v) for v in M.row(i)] for i in range(M.rows)]
out={'schema':'marici.voevodsky.split-fiber-primitive-closure.v1','difference_gram':mat(G),'relation':'d1+d2+d3+d4=0','primitive_roots':{'alpha12':'(d1+d2)/2','alpha13':'(d1+d3)/2','alpha14':'(d1+d4)/2'},'primitive_gram':mat(GA),'primitive_lattice':'A1^3','difference_coordinates_in_primitive_frame':[[int(v) for v in c] for c in coords],'index_of_difference_lattice':4,'interpretation':'The factor 1/2 in node-to-e6 is the primitive saturation seen by pairing component differences; it is not evidence that the ambient lattice has torsion.','checks':checks,'passed':True,'next':'identify e6 and v_alg against the alpha12,alpha13,alpha14 primitive frame using two labelled soft centers'}
(R/'research/voevodsky/results/split_fiber_primitive_closure.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'primitive_gram':out['primitive_gram'],'difference_coordinates':out['difference_coordinates_in_primitive_frame'],'index':4,'next':out['next']}))
