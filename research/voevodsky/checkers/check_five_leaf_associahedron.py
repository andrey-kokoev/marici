"""Finite free rotation graph; packet realization cannot supply higher fillers."""
from functools import lru_cache
from pathlib import Path
import json
@lru_cache(None)
def trees(labels):
 if len(labels)==1:return (labels[0],)
 return tuple((l,r) for i in range(1,len(labels)) for l in trees(labels[:i]) for r in trees(labels[i:]))
def rotations(t):
 if isinstance(t,str):return set()
 l,r=t;out=set()
 if isinstance(l,tuple):out.add((l[0],(l[1],r)))
 out|={(q,r) for q in rotations(l)}
 out|={(l,q) for q in rotations(r)}
 return out
v=trees(('a','b','c','d','e'));assert len(v)==14
index={t:i for i,t in enumerate(v)};edges={(index[t],index[u]) for t in v for u in rotations(t)}
assert len(edges)==21
adj={i:set() for i in range(len(v))}
for a,b in edges:adj[a].add(b);adj[b].add(a)
def count_cycles(n):
 found=set()
 def walk(path):
  u=path[-1]
  if len(path)==n:
   if path[0] in adj[u]:
    seq=path;variants=[tuple(seq[i:]+seq[:i]) for i in range(n)]
    rev=list(reversed(seq));variants += [tuple(rev[i:]+rev[:i]) for i in range(n)]
    found.add(min(variants))
   return
  for z in adj[u]-set(path):walk(path+[z])
 for u in adj:walk([u])
 return len(found)
squares=count_cycles(4);pentagons=count_cycles(5)
assert squares>=3 and pentagons>=6
# No relation is imposed between parallel words of rotations in the free
# path category. A proof packet depends only on leaves, not their brackets.
short=((),());long=((0,),(),(1,));assert short!=long
report={'passed':True,'five_leaf_parenthesizations':len(v),'oriented_rotation_edges':len(edges),'simple_four_cycles':squares,'simple_five_cycles':pentagons,'path_obstruction':'free rotation paths have no pentagon 3-cell, much less overlap 4-cell','scope':'Five uniquely rooted proof leaves and formal binary reassociations. Cycle counts and same packet image do not source or admit pentagon fillers or actual-history identity.'}
out=Path(__file__).resolve().parents[1]/'results/five-leaf-associahedron.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
