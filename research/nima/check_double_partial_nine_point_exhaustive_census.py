#!/usr/bin/env python3
"""Optimized exhaustive n=9 common-tree-complex census over cyclic orders."""
import itertools,json,math
from collections import Counter
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];N=9
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def rec(v):
 if len(v)<=3:return (frozenset(),)
 out=set();a,z=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=rec(v[:k+1]) if k+1>=3 else (frozenset(),);R=rec(v[k:]) if len(v)-k>=3 else (frozenset(),);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,z))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(out)
def canon(S,U):
 S=frozenset(S);C=frozenset(U-S);return min((S,C),key=lambda q:(len(q),tuple(sorted(q))))
alpha=tuple(range(1,N+1));U=set(alpha);A=[]
for t in rec(tuple(range(N))):A.append(frozenset(canon(set(alpha[i:j]),U) for i,j in t))
def interval(S,beta):
 bits=[x in S for x in beta];return sum(bits[i]!=bits[(i+1)%N] for i in range(N))==2
def connected(F):
 if not F:return False
 unseen=set(F);stack=[unseen.pop()]
 while stack:
  a=stack.pop();near=[b for b in unseen if len(a^b)==2]
  for b in near:unseen.remove(b);stack.append(b)
 return not unseen
def inv(F):
 if not F:return (0,False,(),0,0,0)
 faces=set();ridges=Counter();top=N-3
 for f in F:
  q=list(f)
  for r in range(top+1):faces.update(frozenset(s) for s in itertools.combinations(q,r))
  for r in itertools.combinations(q,top-1):ridges[frozenset(r)]+=1
 fv=tuple(sum(len(s)==r for s in faces) for r in range(top+1));chi=sum((-1)**(r-1)*fv[r] for r in range(1,len(fv)))
 return (len(F),connected(F),fv,chi,sum(v==1 for v in ridges.values()),max(ridges.values()))
hist=Counter();examples={};total=0
for tail in itertools.permutations(range(2,N+1)):
 beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
 if beta>rev:continue
 common=frozenset(t for t in A if all(interval(s,beta) for s in t));key=inv(common);hist[key]+=1;examples.setdefault(key,list(beta));total+=1
classes=[]
for k,count in sorted(hist.items()):
 cells,conn,fv,chi,bound,maxridge=k;classes.append({'orbit_count':count,'maximal_cells':cells,'connected':conn,'f_vector':list(fv),'euler_characteristic':chi,'boundary_ridges':bound,'max_ridge_incidence':maxridge,'example_beta':examples[k]})
nonempty=[c for c in classes if c['maximal_cells']];checks={'all_20160_orbits':total==math.factorial(8)//2,'all_nonempty_connected':all(c['connected'] for c in nonempty),'all_ridge_pseudomanifolds':all(c['max_ridge_incidence']<=2 for c in nonempty),'proper_nonempty_euler_one':all(c['euler_characteristic']==1 for c in nonempty if c['boundary_ridges']),'one_closed_candidate':sum(c['orbit_count'] for c in nonempty if not c['boundary_ridges'])==1}
out={'schema':'marici.nima.double-partial-nine-point-exhaustive-census.v1','n':9,'order_orbits':total,'invariant_classes':len(classes),'empty_orbits':next(c['orbit_count'] for c in classes if c['maximal_cells']==0),'classes':classes,'checks':checks,'passed':all(checks.values())}
p=ROOT/'research/nima/results/double-partial-nine-point-exhaustive-census.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'order_orbits':total,'invariant_classes':len(classes),'empty_orbits':out['empty_orbits'],'checks':checks},indent=2));raise SystemExit(0 if out['passed'] else 1)
