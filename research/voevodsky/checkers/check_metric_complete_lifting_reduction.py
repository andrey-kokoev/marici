"""Full atom-norm readout and constructive scalar-envelope reduction."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
D=Q(1,128**4);M=16513*D;R=[Q(1,128**j) for j in range(4)]
def source(p,q,h,k=Q(0)):
 c=[Q(50),Q(51),Q(52),Q(53)];a=50+D*h;b=51+D*k
 u=sum(c)+D*p-a-b;v=sum(x*r for x,r in zip(c,R))+D*q-a-R[1]*b
 z=(v-R[3]*u)/(R[2]-R[3]);return (a,b,z,u-z)
def norm(x):return max(map(abs,x))
def readout(p,q,x):return (source(p,q,Q(0))[2]-x[2])/M
def clamp(x,a,b):return min(b,max(a,x))
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 controls=0
 for p,q in product((Q(0),Q(1,2),Q(1)),repeat=2):
  for h,k in product((Q(-1,4),Q(0),Q(1,2),Q(1),Q(5,4)),repeat=2):
   x=source(p,q,h,k);v=readout(p,q,x)
   assert v==h+Q(129,16513)*k
   for a,b in ((Q(0),Q(1)),(Q(1,4),Q(3,4)),(Q(1,2),Q(1,2))):
    # Coordinate readout bounds distance to EVERY witness, including endpoints.
    for t in (a,(a+b)/2,b):
     witness=source(p,q,t);assert M*abs(v-t)<=norm(tuple(z-w for z,w in zip(x,witness)))
    # Clamping cannot increase scalar distance to an interval in [0,1].
    c=clamp(v,Q(0),Q(1));assert abs(c-clamp(c,a,b))<=abs(v-clamp(v,a,b))
    # Lifting the clamped scalar has EXACT distance M*dist(c,interval).
    xnew=source(p,q,c);nearest=source(p,q,clamp(c,a,b))
    assert norm(tuple(z-w for z,w in zip(xnew,nearest)))==M*abs(c-clamp(c,a,b))
    assert all(0<=z<=100+2*j for j,z in enumerate(xnew));controls+=1
 bounds=[]
 for n in (4,6,9,12,18):
  old=D*Q(3,4*n**3);new=M*Q(3,4*n**3);assert new/old==16513
  bounds.append({'n':n,'strict_epsilon_threshold':str(new),'threshold_decimal':float(new),
   'common_pieces_lower_bound':(n+2)//3,'improvement_factor':16513})
 result={'passed':True,'metric':'same-public-point original atom l_infinity',
 'readout':'(source(p,q,h=0,k=0)[2]-returned_atom[2])/(16513*128^-4)',
 'M':str(M),'controls':controls,'corrected_bounds':bounds,
 'representation_reduction':'Any K-piece approximate source section yields a scalar band section with K formulas; clamping and lifting needs at most 3K polyhedral pieces.',
 'remaining_gap':'Matching optimal scalar band piece complexity versus eta=epsilon/M.'}
 (OUT/'metric-complete-lifting-reduction.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
