"""Independent x/y proof bridges commute on packets under Farkas composition."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
rows=((-Q(1),Q(0)),(Q(1),Q(0)),(Q(0),-Q(1)),(Q(0),Q(1)))
b=(Q(0),Q(1),Q(0),Q(1));dx=(Q(1),Q(1),Q(0),Q(0));dy=(Q(0),Q(0),Q(1),Q(1))
def dot(x,y):return sum((a*z for a,z in zip(x,y)),Q(0))
def valid(m,c,v,T):return min((*m,c))>=0 and tuple(dot(tuple(r[j] for r in rows),m) for j in (0,1))==tuple(v) and dot(b,m)+c==Q(T)
def mix(x,y,t):return tuple((1-t)*a+t*z for a,z in zip(x,y))
def compose(x,y,k,ell,delta,roots_x,roots_y):
 if roots_x!=roots_y or roots_x!=('x-low','x-high','y-low','y-high'):raise PermissionError('SOURCE_ROOT_MISMATCH')
 m=tuple(k*x[i]+ell*y[i] for i in range(4));return (m,delta)
rx=('x-low','x-high','y-low','y-high')
x0=(Q(1),Q(2),Q(0),Q(0));x1=(Q(0),Q(1),Q(1),Q(1))
y0=(Q(0),Q(0),Q(1),Q(2));y1=(Q(1),Q(1),Q(0),Q(1))
for u in (x0,x1):assert valid(u,0,(1,0),2)
for u in (y0,y1):assert valid(u,0,(0,1),2)
checks=0;positive=0
for k,ell,delta,t,s in product((Q(1),Q(2)),(Q(1),Q(2)),(Q(0),Q(1,2)),(Q(0),Q(1,4),Q(1,2),Q(1)),(Q(0),Q(1,4),Q(1,2),Q(1))):
 U=2*k+2*ell+delta;V=(k,ell)
 mx=mix(x0,x1,t);my=mix(y0,y1,s)
 out,c=compose(mx,my,k,ell,delta,rx,rx)
 corners={(i,j):compose(x,y,k,ell,delta,rx,rx)[0] for i,x in enumerate((x0,x1)) for j,y in enumerate((y0,y1))}
 across_x=mix(mix(corners[0,0],corners[1,0],t),mix(corners[0,1],corners[1,1],t),s)
 across_y=mix(mix(corners[0,0],corners[0,1],s),mix(corners[1,0],corners[1,1],s),t)
 assert out==across_x==across_y and valid(out,c,V,U)
 # Surplus injected at postcomposition can be absorbed by a fixed positive
 # source kernel; this has no effect on the two bridge-order comparisons.
 norm=tuple(out[i]+delta*dx[i] for i in range(4))
 assert valid(norm,Q(0),V,U)
 if delta:positive+=1
 checks+=1
assert checks>50 and positive>0
try:compose(x0,y0,Q(1),Q(1),Q(0),rx,('foreign',))
except PermissionError:root_refused=True
else:raise AssertionError('mixed-source proof incorrectly combined')
report={'passed':True,'two_varying_bridge_squares':checks,'added_surplus_cases':positive,'strict_packet_interchange':'mix_y(mix_x(corners))=mix_x(mix_y(corners))=k mix_x(X)+ell mix_y(Y)','foreign_source_refused':root_refused,'fine_history':'different horizontal paths; no 3-cell/4-cell equality supplied','scope':'Fixed irredundant square, both x<=2 and y<=2 have two competing zero-surplus proofs; positive k,ell, nonnegative post-surplus. Packet equalities only.'}
out=Path(__file__).resolve().parents[1]/'results/two-varying-square-proof-bridges.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
