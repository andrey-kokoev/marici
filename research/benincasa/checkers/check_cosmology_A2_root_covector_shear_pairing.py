#!/usr/bin/env python3
"""Classify cyclic orbit-summed root/covector shears on A2."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prev=json.loads((R/'cosmology_dlog_root_centralizer_element.json').read_text());e6=json.loads((R/'clifford_e6_cyclic_equivariance.json').read_text());assert prev['passed']
Q=((0,-1),(1,-1));Qi=((-1,1),(-1,0));I=((1,0),(0,1));r=(0,-1)
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def mv(A,v):return tuple(sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A)))
def op(v,l):return tuple(tuple(v[i]*l[j] for j in range(2)) for i in range(2))
def add(*Ms):return tuple(tuple(sum(M[i][j] for M in Ms) for j in range(2)) for i in range(2))
def orbit_sum(l):
 terms=[]
 for q,qi in ((I,I),(Q,Qi),(mm(Q,Q),mm(Qi,Qi))):terms.append(mm(op(mv(q,r),l),qi))
 return add(*terms)
S1,S2=orbit_sum((1,0)),orbit_sum((0,1));assert S1==((-1,2),(-2,1)) and S2==((-2,1),(-1,-1))
# lambda=(a,b) maps to centralizer coordinates x=-a-2b,y=2a+b.
vals=[]
for a,b in itertools.product(range(-5,6),repeat=2):vals.append((a,b,-a-2*b,2*a+b))
assert all((x-y)%3==0 for a,b,x,y in vals)
assert all(any((x,y)==(X,Y) for a,b,X,Y in vals) for x,y in [(0,0),(1,1),(-1,-1),(2,-1)])
out={'schema':'marici.benincasa.cosmology-A2-root-covector-shear-pairing.v1','root_coordinates':list(r),'covector_coordinates':'lambda=(a,b)','orbit_summed_shear_coordinates':{'x':'-a-2b','y':'2a+b'},'parameter_matrix':[[-1,-2],[2,1]],'parameter_matrix_determinant':3,'image_lattice':'{(x,y) in Z^2 : x congruent y mod 3}','image_index':3,'single_tensor_equivariant_nonzero':False,'orbit_sum_equivariant':True,'invariant_detector_restricts_to_zero':e6['detector_values']==[0,0,0],'sourced_occurrence_sensitive_covector_present':False,'conclusion':'a covector would define an equivariant shear only after orbit summation, but current data supply none; all such integral shears lie in an index-three centralizer sublattice','next_test':'apply the canonical A2 Cartan pairing to the divisor root and determine which index-three shear it produces','passed':True};(R/'cosmology_A2_root_covector_shear_pairing.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
