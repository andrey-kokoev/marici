#!/usr/bin/env python3
"""Exhaustively orient common-tree pseudomanifolds and verify internal-ridge cancellation at n=9."""
import itertools,json,math
from collections import defaultdict
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
def ckey(q):return (len(q),tuple(sorted(q)))
def interval(S,b):
 bits=[x in S for x in b];return sum(bits[i]!=bits[(i+1)%N] for i in range(N))==2
def ridges(F):
 q=sorted(F,key=ckey);return [(frozenset(q[:i]+q[i+1:]),-1 if i%2 else 1) for i in range(len(q))]
def orient(F):
 inc=defaultdict(list)
 for T in F:
  for R,a in ridges(T):inc[R].append((T,a))
 signs={};components=0
 for root in F:
  if root in signs:continue
  components+=1;signs[root]=1;stack=[root]
  while stack:
   T=stack.pop()
   for R,a in ridges(T):
    if len(inc[R])!=2:continue
    (X,x),(Y,y)=inc[R];G=Y if X==T else X;b=y if X==T else x;required=-signs[T]*a*b
    if G in signs and signs[G]!=required:return False,components,inc,None
    if G not in signs:signs[G]=required;stack.append(G)
 boundary={R:sum(signs[T]*a for T,a in xs) for R,xs in inc.items()}
 return all(boundary[R]==0 for R,xs in inc.items() if len(xs)==2),components,inc,boundary
alpha=tuple(range(1,N+1));U=set(alpha);A=[frozenset(canon(set(alpha[i:j]),U) for i,j in t) for t in rec(tuple(range(N)))];total=empty=nonempty=oriented=closed=proper=0;fails=[];boundary_hist=defaultdict(int)
for tail in itertools.permutations(range(2,N+1)):
 beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
 if beta>rev:continue
 total+=1;F={T for T in A if all(interval(s,beta) for s in T)}
 if not F:empty+=1;continue
 nonempty+=1;ok,components,inc,boundary=orient(F)
 if not ok or components!=1:fails.append({'beta':list(beta),'facets':len(F),'orientable':ok,'components':components});continue
 oriented+=1;free=sum(len(xs)==1 for xs in inc.values());boundary_hist[free]+=1
 if free:proper+=1
 else:closed+=1
checks={'all_20160_orbits':total==math.factorial(8)//2,'expected_nonempty':nonempty==4279,'every_nonempty_has_coherent_global_orientation':oriented==nonempty,'every_internal_ridge_cancels':not fails,'one_closed_fundamental_cycle':closed==1,'all_other_oriented_chains_have_boundary':proper==4278}
out={'schema':'marici.nima.double-partial-nine-point-orientation-coherence.v1','n':9,'order_orbits':total,'empty':empty,'nonempty':nonempty,'coherently_oriented':oriented,'closed_cycles':closed,'proper_relative_chains':proper,'boundary_ridge_histogram':dict(sorted(boundary_hist.items())),'failures':fails,'checks':checks,'passed':all(checks.values()),'statement':'Facet signs make every internal ridge cancel. The unique closed case gives an absolute fundamental cycle; every proper case gives a relative fundamental chain supported on its free-ridge boundary.'}
p=ROOT/'research/nima/results/double-partial-nine-point-orientation-coherence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'nonempty':nonempty,'oriented':oriented,'closed':closed,'proper':proper,'failures':len(fails)},indent=2));raise SystemExit(0 if out['passed'] else 1)
