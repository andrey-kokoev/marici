#!/usr/bin/env python3
"""Homogeneity no-go for general linear q-to-Gysin assignments."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_principal_q_diagonal_rescaling_no_go.json').read_text());assert prior['passed']
def add(x,y):
 z=dict(x)
 for e,c in y.items():z[e]=z.get(e,0)+c
 return {e:c for e,c in z.items() if c}
def scale(x,c):return {e:c*v for e,v in x.items() if c*v}
def mul(x,y):
 z={}
 for (i,j),a in x.items():
  for (k,l),b in y.items():z[(i+k,j+l)]=z.get((i+k,j+l),0)+a*b
 return {e:c for e,c in z.items() if c}
def F(rows):
 s=[{(1,0):a,(0,1):b} for a,b in rows];s=[{e:c for e,c in x.items() if c} for x in s]
 L=add(add(add(mul(s[0],s[0]),mul(s[1],s[1])),mul(s[2],s[2])),add(add(scale(mul(s[0],s[1]),-2),scale(mul(s[0],s[2]),-2)),scale(mul(s[1],s[2]),-2)))
 return mul(mul(mul(s[0],s[1]),s[2]),L)
def rank2(rows):return any(rows[i][0]*rows[j][1]-rows[i][1]*rows[j][0] for i in range(3) for j in range(i))
tested=0
for flat in itertools.product((-1,0,1),repeat=6):
 rows=[flat[0:2],flat[2:4],flat[4:6]]
 if rank2(rows) and all(r!=(0,0) for r in rows):
  f=F(rows);assert f and all(sum(e)==5 for e in f);tested+=1
out={'schema':'marici.benincasa.cosmology-principal-q-general-linear-homogeneity-no-go.v1','conjecture':'a nondegenerate homogeneous linear assignment from two fiber functions to three Gysin variables yields a base-only denominator','assignment':'s_i=a_i*A+b_i*B','Gysin_denominator_degree_in_s':5,'pullback_dichotomy':{'nonzero':'homogeneous fiber degree 5, hence not base-only','zero':'degenerate divisor pullback, hence not a support comparison'},'scaling_falsifier':'F(t*A,t*B)=t^5*F(A,B), whereas a base function is invariant under fiber scaling','bounded_rank2_nonzero_row_matrices_tested':tested,'bounded_failures':0,'conjecture_disposition':'falsified for every nondegenerate homogeneous linear assignment','source_authority_supplied':False,'next_conjecture':'adding base-dependent affine constants to a rank-two linear assignment can cancel its leading fiber degree','next_falsifier':'extract the degree-five leading term and prove it equals the homogeneous linear pullback already shown nonzero','passed':True};(R/'cosmology_principal_q_general_linear_homogeneity_no_go.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
