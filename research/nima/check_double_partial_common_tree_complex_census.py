#!/usr/bin/env python3
"""Census topology of arbitrary-order double-partial common-tree complexes."""
import itertools,json,math
from collections import Counter,deque
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def tri(n):
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
 return rec(tuple(range(n)))
def canon(S,U):
 S=frozenset(S);C=frozenset(U-S);return min((S,C),key=lambda q:(len(q),tuple(sorted(q))))
def trees(order):
 U=set(order);return {frozenset(canon(set(order[i:j]),U) for i,j in t) for t in tri(len(order))}
def connected(facets):
 if not facets:return False
 unseen=set(facets);stack=[unseen.pop()]
 while stack:
  a=stack.pop();near=[b for b in unseen if len(a^b)==2]
  for b in near:unseen.remove(b);stack.append(b)
 return not unseen
def invariants(facets):
 if not facets:return {'maximal_cells':0,'connected':False,'f_vector':[],'euler_characteristic':0,'boundary_ridges':0,'max_ridge_incidence':0}
 faces=set();ridge_counts=Counter();top=len(next(iter(facets)))
 for F in facets:
  q=list(F)
  for r in range(len(q)+1):faces.update(frozenset(s) for s in itertools.combinations(q,r))
  for ridge in itertools.combinations(q,top-1):ridge_counts[frozenset(ridge)]+=1
 f=[sum(len(s)==r for s in faces) for r in range(max(map(len,faces))+1)]
 # Include empty face separately; topological Euler uses nonempty faces with dimension |S|-1.
 chi=sum((-1)**(r-1)*f[r] for r in range(1,len(f)))
 return {'maximal_cells':len(facets),'connected':connected(facets),'f_vector':f,'euler_characteristic':chi,'boundary_ridges':sum(v==1 for v in ridge_counts.values()),'max_ridge_incidence':max(ridge_counts.values(),default=0)}
rows=[];summary={}
for n in range(4,9):
 alpha=tuple(range(1,n+1));A=trees(alpha);hist=Counter();examples={};total=0
 # Fix label 1 first (rotation quotient), then identify beta with reversed beta (reflection quotient).
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  F=A&trees(beta);inv=invariants(F);key=(inv['maximal_cells'],inv['connected'],tuple(inv['f_vector']),inv['euler_characteristic'],inv['boundary_ridges'],inv['max_ridge_incidence']);hist[key]+=1;total+=1
  examples.setdefault(key,list(beta))
 classes=[]
 for key,count in sorted(hist.items(),key=lambda kv:(kv[0][0],kv[0][2])):
  cells,conn,fv,chi,boundary_ridges,max_ridge=key;classes.append({'orbit_count':count,'maximal_cells':cells,'connected':conn,'f_vector':list(fv),'euler_characteristic':chi,'boundary_ridges':boundary_ridges,'max_ridge_incidence':max_ridge,'example_beta':examples[key]})
 summary[str(n)]={'order_orbits':total,'isomorphism_invariant_classes':len(classes),'empty_orbits':sum(c['orbit_count'] for c in classes if c['maximal_cells']==0),'disconnected_nonempty_orbits':sum(c['orbit_count'] for c in classes if c['maximal_cells'] and not c['connected'])}
 rows.append({'n':n,'classes':classes})
nonempty=[c for row in rows for c in row['classes'] if c['maximal_cells']]
checks={'all_order_orbits_exhausted':all(summary[str(n)]['order_orbits']==math.factorial(n-1)//2 for n in range(4,9)),'nonempty_complexes_pure_by_construction':True,'all_nonempty_are_ridge_pseudomanifolds':all(c['max_ridge_incidence']<=2 for c in nonempty),'all_proper_nonempty_complexes_have_euler_one':all(c['euler_characteristic']==1 for c in nonempty if c['boundary_ridges']>0),'exactly_one_closed_sphere_candidate_per_n':all(sum(c['orbit_count'] for c in row['classes'] if c['maximal_cells'] and c['boundary_ridges']==0)==1 for row in rows),'census_nonempty':bool(rows)}
out={'schema':'marici.nima.double-partial-common-tree-complex-census.v1','fixed_order':'alpha=(1,...,n)','quotient':'beta modulo rotation (fix 1 first) and reversal','range':[4,8],'summary':summary,'results':rows,'checks':checks,'passed':all(checks.values()),'scope':'Exact exhaustive cyclic-order census using combinatorial f-vectors and facet-flip connectivity; classes sharing these invariants need not be combinatorially isomorphic.'}
p=ROOT/'research/nima/results/double-partial-common-tree-complex-census.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'range':[4,8],'summary':summary},indent=2));raise SystemExit(0 if out['passed'] else 1)
