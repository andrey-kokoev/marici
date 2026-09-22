"""Exact rational geometry for a declared query-relative analytical carrier.
No floating-point hull or optimizer is used.
"""
from fractions import Fraction as Q
from itertools import combinations

def solve(A,b):
 m=[list(map(Q,row))+[Q(v)] for row,v in zip(A,b)];n=len(b)
 for j in range(n):
  k=next((k for k in range(j,n) if m[k][j]),None)
  if k is None:return None
  m[j],m[k]=m[k],m[j];v=m[j][j];m[j]=[a/v for a in m[j]]
  for k in range(n):
   if k!=j:
    v=m[k][j];m[k]=[a-v*z for a,z in zip(m[k],m[j])]
 return tuple(row[-1] for row in m)
def vertices(A,b):
 out=set()
 for inds in combinations(range(len(b)),3):
  x=solve([A[i] for i in inds],[b[i] for i in inds])
  if x is not None and all(sum(a*z for a,z in zip(row,x))<=v for row,v in zip(A,b)):out.add(x)
 return sorted(out)
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(lifted):
 # Retain an explicit source lift at each observable vertex.
 bypoint={tuple(z):tuple(x) for z,x in lifted};points=sorted(bypoint)
 if len(points)<=1:return [(p,bypoint[p]) for p in points]
 lower=[];upper=[]
 for p in points:
  while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
  lower.append(p)
 for p in reversed(points):
  while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
  upper.append(p)
 return [(p,bypoint[p]) for p in lower[:-1]+upper[:-1]]
def image(x,c):return sum(x),sum(a*z for a,z in zip(c,x))
def project(A,b,c):return hull([(image(x,c),x) for x in vertices(A,b)])
def clip(poly,row,bound):
 if not poly:return []
 def slack(p):return bound-sum(a*z for a,z in zip(row,p))
 if len(poly)==1:return poly if slack(poly[0][0])>=0 else []
 out=[]
 for (p,x),(q,y) in zip(poly,poly[1:]+poly[:1]):
  a=slack(p);b=slack(q)
  if a>=0:out.append((p,x))
  if (a<0<b) or (b<0<a):
   t=a/(a-b);out.append((tuple(v+t*(w-v) for v,w in zip(p,q)),tuple(v+t*(w-v) for v,w in zip(x,y))))
 return hull(out)
def facets(poly):
 assert len(poly)>=3
 out=[]
 for (a,_),(b,_) in zip(poly,poly[1:]+poly[:1]):
  normal=(b[1]-a[1],a[0]-b[0]);bound=sum(n*z for n,z in zip(normal,a));out.append((normal,bound))
 return out
