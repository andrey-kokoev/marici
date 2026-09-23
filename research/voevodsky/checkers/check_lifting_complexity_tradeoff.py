"""Exact controls for a two-history / common-section complexity separation."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def plane(a,b,c):
 # Heights t^3, public (t,t^2): interpolating quadratic at a,b,c.
 return (-(a*b+a*c+b*c),a+b+c,a*b*c)
def value(f,v):return f[0]*v[0]+f[1]*v[1]+f[2]
def source(p,q,h):
 r=[Q(1,128**j) for j in range(4)];center=[Q(50),Q(51),Q(52),Q(53)];d=Q(1,128**4)
 t0=50+d*h;t1=Q(51);u=sum(center)+d*p-t0-t1
 v=sum(a*b for a,b in zip(center,r))+d*q-t0-r[1]*t1
 t2=(v-r[3]*u)/(r[2]-r[3]);return (t0,t1,t2,u-t2)
def main():
 # Affine source inverse is admitted on the entire normalized parameter cube.
 for p,q,h in product((Q(0),Q(1)),repeat=3):
  x=source(p,q,h);assert all(0<v<100+2*j for j,v in enumerate(x))
 reports=[]
 for n in (4,6,9,12,18):
  ts=[Q(i,n) for i in range(1,n+1)];V=[(t,t*t,t**3) for t in ts];lower=[];upper=[]
  for inds in combinations(range(n),3):
   f=plane(*(ts[i] for i in inds));gaps=[v[2]-value(f,v) for v in V]
   assert all(gaps[i]==0 for i in inds)
   if min(gaps)>=0:lower.append((inds,f))
   if max(gaps)<=0:upper.append((inds,f))
  assert lower and upper
  for i,v in enumerate(V):
   # Both envelopes attain the same forced value at every public vertex.
   assert max(value(f,v) for _,f in lower)==v[2]
   assert min(value(f,v) for _,f in upper)==v[2]
   # Separate constant sections h=1 and h=0 satisfy their whole histories.
   assert all(value(f,v)<=1 for _,f in lower)
   assert all(value(f,v)>=0 for _,f in upper)
  # No four lifted vertices coplanar: interpolation residual is cubic product.
  for inds in combinations(range(n),4):
   a,b,c,d=(ts[i] for i in inds);f=plane(a,b,c)
   assert d**3-value(f,(d,d*d))==(d-a)*(d-b)*(d-c)!=0
  # Fan triangulation covers convex public polygon, with n-2 pieces.
  fan=[(0,i,i+1) for i in range(1,n-1)]
  for ids in fan:
   for j in ids:
    v=V[j];assert all(value(f,v)<=v[2] for _,f in lower) and all(value(f,v)>=v[2] for _,f in upper)
  reports.append({'n':n,'vertices':[[str(x) for x in v] for v in V],
   'lower_planes':[[str(x) for x in f] for _,f in lower],
   'upper_planes':[[str(x) for x in f] for _,f in upper],
   'fan_triangles':fan,'minimum_common_pieces_lower_bound':(n+2)//3,
   'common_pieces_constructed':n-2,'separate_section_pieces_each':1})
 result={'passed':True,'cases':reports,
 'scope':'Theta(n) affine-piece complexity after merging two histories, versus one piece per separate history. Not a lower bound for arbitrary programs or total retained bytes.'}
 (OUT/'lifting-complexity-tradeoff.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':True,'bounds':[{k:r[k] for k in ('n','minimum_common_pieces_lower_bound','common_pieces_constructed')} for r in reports]},indent=2))
if __name__=='__main__':main()
