"""Compose uniquely overlap-defined cube isometries around triangles and four-reference loops. These are chart transitions, not assumed cage automorphisms."""
from itertools import product,permutations,combinations
from collections import Counter
from ramsey_strip_cube_chart_overlap import charts,T
bits=list(product((0,1),repeat=3));I=tuple(range(8));trans={}
for a in range(15):
 for b in range(15):
  if T[a]&T[b]:continue
  shared=charts[a].keys()&charts[b].keys();hits=[]
  for p in permutations(range(3)):
   for s in bits:
    F=lambda x:tuple(x[p[k]]^s[k] for k in range(3))
    if all(F(charts[a][j])==charts[b][j] for j in shared):hits.append(tuple(bits.index(F(x)) for x in bits))
  trans[a,b],=hits
compose=lambda a,b:tuple(a[x] for x in b)
def loop(path):
 h=I
 for a,b in zip(path,path[1:]+path[:1]):h=compose(trans[a,b],h)
 return h
def order(h):
 p=h;n=1
 while p!=I:p=compose(h,p);n+=1
 return n
tri=Counter();quad=Counter();examples={}
for a,b,c in combinations(range(15),3):
 if all(x in trans for x in ((a,b),(b,c),(c,a))):
  h=loop([a,b,c]);tri[order(h),sum(h[i]==i for i in I)]+=1
for path in permutations(range(15),4):
 if path[0]!=min(path) or path[1]>path[-1]:continue
 if all((a,b) in trans for a,b in zip(path,path[1:]+path[:1])):
  h=loop(list(path));quad[order(h),sum(h[i]==i for i in I)]+=1;examples.setdefault(order(h),([x+15 for x in path],h))
print('triangle holonomy (order,fixed vertices)',tri);print('four-reference holonomy',quad);print('examples',examples)
