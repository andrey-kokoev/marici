"""Exact atom-norm tolerance bounds; independent of the exact-family producer."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
DELTA=Q(1,128**4);R=[Q(1,128**j) for j in range(4)]
def weights(ts):return [1/product_of(t-u for u in ts if u!=t) for t in ts]
def product_of(xs):
 out=Q(1)
 for x in xs:out*=x
 return out
def source(p,q,h):
 c=[Q(50),Q(51),Q(52),Q(53)];a=50+DELTA*h;b=Q(51)
 u=sum(c)+DELTA*p-a-b;v=sum(x*r for x,r in zip(c,R))+DELTA*q-a-R[1]*b
 z=(v-R[3]*u)/(R[2]-R[3]);return (a,b,z,u-z)
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 records=[]
 for n in (4,6,9,12,18):
  ts=[Q(i,n) for i in range(1,n+1)];threshold=DELTA*Q(3,4*n**3);checks=0
  for points in combinations(ts,4):
   w=weights(points)
   assert all(sum(a*t**k for a,t in zip(w,points))==0 for k in (0,1,2))
   assert sum(a*t**3 for a,t in zip(w,points))==1
   assert sum(map(abs,w))<=Q(4*n**3,3)
   checks+=1
  # Safe positive tolerance: every four-vertex assignment is impossible.
  eps=threshold/2;assert (eps/DELTA)*Q(4*n**3,3)<1
  # Sharpness of the four-equally-spaced-vertex obstruction, not the whole family.
  points=ts[:4];w=weights(points);eta=Q(3,4*n**3)
  errors=[eta*(1 if a>0 else -1) for a in w]
  assert sum(a*e for a,e in zip(w,errors))==1
  quadratic_values=[t**3-e for t,e in zip(points,errors)]
  assert sum(a*v for a,v in zip(w,quadratic_values))==0
  records.append({'n':n,'strict_atom_epsilon_threshold':str(threshold),
   'tested_positive_atom_epsilon':str(eps),'common_piece_lower_bound':(n+2)//3,
   'exact_piece_upper_bound':n-2,'quartets_checked':checks})
 # Original-coordinate metric conversion for the fixed-t1 affine source inverse.
 z0=source(Q(0),Q(0),Q(0));z1=source(Q(0),Q(0),Q(1));direction=tuple(b-a for a,b in zip(z0,z1));M=max(map(abs,direction))
 assert direction[0]==DELTA and direction[1]==0
 for p,q,h in product((Q(0),Q(1)),repeat=3):
  x=source(p,q,h);assert all(0<v<100+2*j for j,v in enumerate(x))
  midpoint=source(p,q,Q(1,2));assert max(abs(a-b) for a,b in zip(x,midpoint))==M/2
 # At epsilon>=M/2, h=1/2 is within tolerance of each history:
 # choose its closest admissible h in [f,1] or [0,g], always in [0,1].
 sparsified=[];n=60
 for eta in (Q(1,10**8),Q(1,10**5),Q(1,1000),Q(1,100)):
  candidates=[]
  for stride in range(1,n):
   if eta<Q(3,4)*(Q(stride,n)**3):
    count=(n-1)//stride+1
    if count>=4:candidates.append((count,stride))
  count,stride=max(candidates,default=(0,0))
  sparsified.append({'n':n,'atom_epsilon':str(DELTA*eta),'normalized_eta':str(eta),
   'stride':stride,'selected_vertices':count,'piece_lower_bound':max(1,(count+2)//3)})
 result={'passed':True,'norm':'original atom-coordinate l_infinity; distance to each SAME-public-point history fiber',
 'delta':str(DELTA),'families':records,'sparsified_lower_bounds':sparsified,
 'fixed_t1_inverse_h_direction':list(map(str,direction)),
 'one_affine_piece_sufficient_atom_epsilon':str(M/2),
 'scope':'Positive-tolerance lower bound and coarse collapse upper bound. No matching epsilon-dependent optimum, total-byte claim, or independent packet verifier.'}
 (OUT/'robust-lifting-tradeoff.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':True,'families':records,'one_piece_sufficient_epsilon':str(M/2)},indent=2))
if __name__=='__main__':main()
