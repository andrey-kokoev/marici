#!/usr/bin/env python3
"""Leading-degree no-go for affine q-to-Gysin assignments."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_principal_q_general_linear_homogeneity_no_go.json').read_text());assert prior['passed']
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
def polyF(rows,constants):
 ss=[]
 for (a,b),c in zip(rows,constants):ss.append({e:v for e,v in {(1,0):a,(0,1):b,(0,0):c}.items() if v})
 L=add(add(add(mul(ss[0],ss[0]),mul(ss[1],ss[1])),mul(ss[2],ss[2])),add(add(scale(mul(ss[0],ss[1]),-2),scale(mul(ss[0],ss[2]),-2)),scale(mul(ss[1],ss[2]),-2)))
 return mul(mul(mul(ss[0],ss[1]),ss[2]),L)
def rank2(r):return any(r[i][0]*r[j][1]-r[i][1]*r[j][0] for i in range(3) for j in range(i))
tested=0
for flat in itertools.product((-1,0,1),repeat=6):
 rows=[flat[:2],flat[2:4],flat[4:]]
 if rank2(rows) and all(r!=(0,0) for r in rows):
  lead=polyF(rows,(0,0,0));assert lead
  for cs in itertools.product((-1,0,1),repeat=3):
   f=polyF(rows,cs);top={e:c for e,c in f.items() if sum(e)==5};assert top==lead;tested+=1
out={'schema':'marici.benincasa.cosmology-principal-q-affine-leading-degree-no-go.v1','conjecture':'base-dependent affine constants cancel fiber dependence for a rank-two linear q-to-Gysin assignment','assignment':'s_i=L_i(A,B)+c_i(u)','leading_term_identity':'degree_fiber_5 F(L+c)=F(L)','reason':'F=s1*s2*s3*Lambda_P is homogeneous of degree five; constants contribute only lower fiber degree','rank_two_nonzero_row_leading_pullback':'nonzero by the general linear homogeneity gate','cancellation_possible':False,'bounded_affine_assignments_tested':tested,'bounded_failures':0,'conjecture_disposition':'falsified for every rank-two assignment with nonzero rows','degenerate_cases_not_claimed':'rank at most one, a zero leading row, or identically zero denominator','next_conjecture':'a rank-one affine assignment can make the Gysin denominator a nonzero base function','next_falsifier':'classify affine lines in s-space on which the degree-five Gysin polynomial is constant','passed':True};(R/'cosmology_principal_q_affine_leading_degree_no_go.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
