"""Deliberate thin Tamari reachability enrichment is nonfaithful to path replay."""
from functools import lru_cache
from pathlib import Path
import json
@lru_cache(None)
def trees(s):
 if len(s)==1:return (s[0],)
 return tuple((a,b) for i in range(1,len(s)) for a in trees(s[:i]) for b in trees(s[i:]))
def moves(t):
 if isinstance(t,str):return set()
 x,y=t;out=set()
 if isinstance(x,tuple):out.add((x[0],(x[1],y)))
 out|={(q,y) for q in moves(x)}|{(x,q) for q in moves(y)}
 return out
v=trees(tuple('abcde'));edges={t:moves(t) for t in v};assert len(v)==14 and sum(map(len,edges.values()))==21
@lru_cache(None)
def counts(t):
 result={t:1}
 for u in edges[t]:
  for z,n in counts(u).items():result[z]=result.get(z,0)+n
 return result
relation={(i,j) for i in v for j in counts(i)}
assert all(a==b or (b,a) not in relation for a,b in relation)
assert all((a,c) in relation for a,b in relation for x,c in relation if b==x)
parallel={(a,b):n for a in v for b,n in counts(a).items() if n>1}
assert parallel
start=(((('a','b'),'c'),'d'),'e');goal=('a',('b',('c',('d','e'))))
assert counts(start)[goal]>1
# Thin enrichment maps every rotation word a->b to the unique reachability
# arrow a<=b. It is mathematically compositional but NOT faithful to words.
assert (start,goal) in relation and counts(start)[goal]>1
report={'passed':True,'parenthesizations':len(v),'generating_rotations':sum(map(len,edges.values())),'reachable_order_pairs':len(relation),'parallel_endpoint_pairs':len(parallel),'extreme_parallel_paths':counts(start)[goal],'thin_category_composes':True,'forgetful_path_map_faithful':False,'scope':'New Tamari reachability category on ordered five-leaf brackets; does not identify historical Farkas proof executions, authenticate row roots or supply analytic S,A,R,C,G role map.'}
out=Path(__file__).resolve().parents[1]/'results/tamari-thin-enrichment.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
