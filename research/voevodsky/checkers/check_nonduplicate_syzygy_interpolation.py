"""Nonduplicate primitive rows: competing normalizers admit convex proof interpolation."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
A=(Q(-1),Q(1),Q(2));b=(Q(0),Q(1),Q(3));dA=(Q(1),Q(1),Q(0));dB=(Q(2),Q(0),Q(1))
def dot(x,y):return sum((s*t for s,t in zip(x,y)),Q(0))
def valid(m,c,T):return min((*m,c))>=0 and dot(A,m)==1 and dot(b,m)+c==Q(T)
def normalize(m,c,T,d):
 assert valid(m,c,T) and min(d)>=0 and dot(A,d)==0 and dot(b,d)>0
 q=tuple(m[i]+c*d[i]/dot(b,d) for i in range(3));assert valid(q,Q(0),T);return q
def bridge(x,y,t,T):
 assert valid(x,Q(0),T) and valid(y,Q(0),T) and 0<=Q(t)<=1
 z=tuple((1-Q(t))*x[i]+Q(t)*y[i] for i in range(3))
 assert valid(z,Q(0),T);return z
assert dot(b,dA)==1 and dot(b,dB)==3
p=(Q(0),Q(1),Q(0));T=Q(2);c=Q(1)
x=normalize(p,c,T,dA);y=normalize(p,c,T,dB)
assert x==(1,2,0) and y==(Q(2,3),1,Q(1,3)) and x!=y
k=tuple(y[i]-x[i] for i in range(3));assert k==(Q(-1,3),Q(-1),Q(1,3))
assert dot(A,k)==dot(b,k)==0
checks=0
for bound,initial_upper,t in product((Q(2),Q(3),Q(4)),(Q(1),Q(3,2),Q(2)),(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))):
 if initial_upper>bound:continue
 m=(initial_upper-1,initial_upper,Q(0));surplus=bound-initial_upper
 xa=normalize(m,surplus,bound,dA);yb=normalize(m,surplus,bound,dB)
 bridge(xa,yb,t,bound);checks+=1
assert checks>20
try:bridge(x,y,Q(4),T)
except AssertionError:out_of_range_refused=True
else:raise AssertionError('extrapolation admitted')
# Stronger witness: all four primitive facets of the unit square are
# irredundant; a y-cycle can consume surplus in a proof of an x-target.
square=((-Q(1),Q(0)),(Q(1),Q(0)),(Q(0),-Q(1)),(Q(0),Q(1)))
sqb=(Q(0),Q(1),Q(0),Q(1));dx=(Q(1),Q(1),Q(0),Q(0));dy=(Q(0),Q(0),Q(1),Q(1))
def sqvalid(m,c,T):return min((*m,c))>=0 and tuple(dot(tuple(row[j] for row in square),m) for j in (0,1))==(Q(1),Q(0)) and dot(sqb,m)+c==Q(T)
sp=(Q(0),Q(1),Q(0),Q(0));sx=tuple(sp[i]+dx[i] for i in range(4));sy=tuple(sp[i]+dy[i] for i in range(4))
assert sqvalid(sp,Q(1),Q(2)) and sqvalid(sx,Q(0),Q(2)) and sqvalid(sy,Q(0),Q(2)) and sx!=sy
square_checks=0
for t in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
 z=tuple((1-t)*sx[i]+t*sy[i] for i in range(4));assert sqvalid(z,Q(0),Q(2));square_checks+=1
report={'passed':True,'irredundant_square_rows':['-x<=0','x<=1','-y<=0','y<=1'],'square_normalizers':[list(map(str,sx)),list(map(str,sy))],'square_interpolations_checked':square_checks,'nonduplicate_primitive_rows':['-x<=0','x<=1','2x<=3'],'distinct_normalizers':[list(map(str,x)),list(map(str,y))],'signed_bound_zero_direction':list(map(str,k)),'convex_interpolations_checked':checks,'out_of_range_refused':out_of_range_refused,'first_failed_obligation':'no canonical or admitted proof 2-cell follows from convex packet interpolation; source-rooted constructor and coherence still required','scope':'Finite rational nonduplicate rows, including four irredundant square facets. Packet convexity is mathematical, not proof-history or analytic authority.'}
out=Path(__file__).resolve().parents[1]/'results/nonduplicate-syzygy-interpolation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
