#!/usr/bin/env python3
"""Exact external/composite checks for the reusable super-five-bracket."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_constructors import four_bracket
from momentum_twistor_super import (external_supertwistor, scale_supertwistor,
 super_line_plane_point, super_five_bracket)
xs=map(s.Integer,(1,2,4,7,11,16,22,29));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
def legacy(q):
 a,b,c,d,e=q;num={a:four_bracket(Z[b],Z[c],Z[d],Z[e]),b:four_bracket(Z[c],Z[d],Z[e],Z[a]),c:four_bracket(Z[d],Z[e],Z[a],Z[b]),d:four_bracket(Z[e],Z[a],Z[b],Z[c]),e:four_bracket(Z[a],Z[b],Z[c],Z[d])};den=s.prod(num.values())
 return {m:s.factor(s.prod(num[i] for i in m)/den) for m in itertools.product(q,repeat=4)}
external=super_five_bracket(tuple(S[i] for i in (1,2,3,4,5)));reference=legacy((1,2,3,4,5))
# Source representative: [1,2,3,(45)cap(678),8].
def build_composite(T):
 X=super_line_plane_point(T[4],T[5],T[6],T[7],T[8])
 return X,super_five_bracket((T[1],T[2],T[3],X,T[8]))
X,composite=build_composite(S)
vertices=(S[1],S[2],S[3],X,S[8])
# Odd permutations must reverse every coefficient; a five-cycle is even.
swap_constructed=super_five_bracket((S[1],S[2],S[3],S[8],X))
cyclic=super_five_bracket((S[2],S[3],X,S[8],S[1]))
projective=[]
for i in range(1,9):
 T=dict(S);T[i]=scale_supertwistor(s.Integer(2),T[i]);_,scaled=build_composite(T)
 projective.append(all(s.factor(scaled[m]-v)==0 for m,v in composite.items()) and set(scaled)==set(composite))
G=s.Matrix([[1,2,0,1],[0,1,1,0],[0,0,1,3],[0,0,0,1]])
T={i:type(S[i])(G*S[i].z,S[i].chi) for i in S};_,sl4_composite=build_composite(T)
checks={'external_formula_exactly_reproduced':external==reference,'composite_external_support':set().union(*(set(m) for m in composite))=={1,2,3,4,5,8},'composite_has_degree_four':all(len(m)==4 for m in composite),'composite_expected_sparse_size':len(composite)==6**4,'composite_generic_nonzero':any(v!=0 for v in composite.values()),'odd_swap_of_constructed_argument_reverses_sign':set(swap_constructed)==set(composite) and all(s.factor(swap_constructed[m]+v)==0 for m,v in composite.items()),'cyclic_move_with_constructed_argument_is_invariant':cyclic==composite,'projectively_invariant_in_all_eight_external_supertwistors':all(projective),'sl4_invariant_all_coefficients':s.det(G)==1 and sl4_composite==composite}
out={'schema':'marici.nima.composite-super-five-bracket.v1','source':'arXiv:1212.5605 Table g2n_yangian_invariants','composite':'[1,2,3,(45)cap(678),8]','external_coefficients_checked':len(reference),'composite_coefficients':len(composite),'constructed_chi_support':sorted(X.chi),'sample_component':'chi_1^1 chi_2^2 chi_4^3 chi_8^4','sample_value':str(composite[(1,2,4,8)]),'checks':checks,'passed':all(checks.values()),'scope':'Exact sparse Grassmann evaluation at generic rational kinematics; one source-listed composite five-bracket, not yet its complete N2MHV product.'}
p=ROOT/'research/nima/results/composite-super-five-bracket.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
