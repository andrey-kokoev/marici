"""Exact oriented five-leaf square/pentagon boundaries; no filler inferred."""
from functools import lru_cache
from pathlib import Path
import json
@lru_cache(None)
def trees(s):
 if len(s)==1:return (s[0],)
 return tuple((l,r) for i in range(1,len(s)) for l in trees(s[:i]) for r in trees(s[i:]))
def rotations(t):
 if isinstance(t,str):return set()
 x,y=t;out=set()
 if isinstance(x,tuple):out.add((x[0],(x[1],y)))
 out|={(v,y) for v in rotations(x)}|{(x,v) for v in rotations(y)}
 return out
vertices=trees(('a','b','c','d','e'));idx={v:i for i,v in enumerate(vertices)}
arcs={(idx[t],idx[u]) for t in vertices for u in rotations(t)}
neighbors={i:set() for i in range(len(vertices))}
for a,b in arcs:neighbors[a].add(b);neighbors[b].add(a)
def cycles(n):
 out=set()
 def walk(path):
  if len(path)==n:
   if path[0] in neighbors[path[-1]]:
    allseq=[tuple(path[i:]+path[:i]) for i in range(n)]
    rev=list(reversed(path));allseq += [tuple(rev[i:]+rev[:i]) for i in range(n)]
    out.add(min(allseq))
   return
  for z in neighbors[path[-1]]-set(path):walk(path+[z])
 for a in neighbors:walk([a])
 return sorted(out)
def boundary(cycle):
 sub=set(cycle);sources=[v for v in cycle if not any((w,v) in arcs for w in sub)];sinks=[v for v in cycle if not any((v,w) in arcs for w in sub)]
 assert len(sources)==len(sinks)==1
 s,t=sources[0],sinks[0];paths=[]
 def traverse(path):
  if path[-1]==t:paths.append(tuple(path));return
  for w in sub:
   if (path[-1],w) in arcs and w not in path:traverse(path+[w])
 traverse([s]);assert len(paths)==2
 return paths
sq=cycles(4);pent=cycles(5);assert len(sq)==3 and len(pent)==6
square_paths=boundary(sq[0]);pentagon_paths=boundary(pent[0])
assert sorted(len(p)-1 for p in square_paths)==[2,2]
assert sorted(len(p)-1 for p in pentagon_paths)==[2,3]
roots={x:f'primitive-root:{x}' for x in 'abcde'}
def gate(face,provided_roots,constructor):
 if set(provided_roots)!=set(roots):return 'MISSING_LEAF_ROOT'
 if constructor in ('equal_packet','self_asserted'):return 'MISSING_INDEPENDENT_FACE_CONSTRUCTOR'
 return 'UNVERIFIED_NEW_HIGHER_GENERATOR'
assert gate(square_paths,roots,'equal_packet')=='MISSING_INDEPENDENT_FACE_CONSTRUCTOR'
assert gate(pentagon_paths,roots,'self_asserted')=='MISSING_INDEPENDENT_FACE_CONSTRUCTOR'
assert gate(pentagon_paths,{x:roots[x] for x in 'abcd'},'new_generator')=='MISSING_LEAF_ROOT'
report={'passed':True,'five_leaf_oriented_square_count':len(sq),'five_leaf_oriented_pentagon_count':len(pent),'square_route_lengths':[len(p)-1 for p in square_paths],'pentagon_route_lengths':[len(p)-1 for p in pentagon_paths],'typed_boundaries':'same source and target tagged tree on each face; distinct rotation words','refused':['omitted-leaf-root','self-asserted-filler','equal-packet-as-filler'],'scope':'Finite labelled five-leaf rotation graph. Primitive leaves root edges; no independent 3-cell face constructor or 4-cell overlap coherence supplied.'}
out=Path(__file__).resolve().parents[1]/'results/typed-associahedron-faces.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
