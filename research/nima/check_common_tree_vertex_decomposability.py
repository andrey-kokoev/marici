#!/usr/bin/env python3
"""Search recursively for vertex decompositions of common-tree complexes."""
import itertools,json
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
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
def trees(o):
 U=set(o);return frozenset(frozenset(canon(set(o[i:j]),U) for i,j in t) for t in rec(tuple(range(len(o)))))
def maximal(fs):return frozenset(f for f in fs if not any(f<g for g in fs))
def statekey(fs):return tuple(sorted((tuple(sorted((len(q),tuple(sorted(q))) for q in f)) for f in fs)))
cache={};choice={}
def vd(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in cache:return cache[k]
 sizes={len(f) for f in fs}
 if len(sizes)!=1:return False
 if len(fs)<=1:cache[k]=True;return True
 verts=set().union(*fs)
 for v in sorted(verts,key=lambda q:(len(q),tuple(sorted(q)))):
  deletion=maximal(frozenset(f for f in fs if v not in f))
  link=maximal(frozenset(frozenset(f-{v}) for f in fs if v in f))
  # Actual deletion also contains all link faces. Purity requires each link
  # facet to extend into a same-dimensional facet avoiding v.
  d=next(iter(sizes))
  if not deletion or {len(f) for f in deletion}!={d}:continue
  if not link or {len(f) for f in link}!={d-1}:continue
  if not all(any(q<=g for g in deletion) for q in link):continue
  if vd(deletion) and vd(link):choice[k]=v;cache[k]=True;return True
 cache[k]=False;return False
rows=[];fails=[]
for n in range(4,9):
 alpha=tuple(range(1,n+1));A=trees(alpha);total=empty=good=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=A&trees(beta)
  if not F:empty+=1;continue
  if vd(F):good+=1
  else:fails.append({'n':n,'beta':list(beta),'facets':len(F)})
 rows.append({'n':n,'orbits':total,'empty':empty,'nonempty':total-empty,'vertex_decomposable':good,'failures':total-empty-good})
checks={'all_nonempty_vertex_decomposable':not fails}
out={'schema':'marici.nima.common-tree-vertex-decomposability.v1','range':[4,8],'results':rows,'memoized_states':len(cache),'failures':fails[:20],'checks':checks,'passed':all(checks.values()),'interpretation':'Recursive Provan-Billera vertex-decomposability; each successful split is a deletion/link decomposition along a common channel.'}
p=ROOT/'research/nima/results/common-tree-vertex-decomposability.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'memoized_states':len(cache),'first_failure':fails[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
