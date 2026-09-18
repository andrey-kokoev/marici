#!/usr/bin/env python3
"""Verify square/pentagon coherence faces of type-A history cluster completions."""
import itertools,json
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def diag(a,b,P):
 a,b=sorted((a,b));return None if b-a==1 or (a==1 and b==P) else (a,b)
@lru_cache(None)
def triangulations(vertices,P):
 V=tuple(vertices)
 if len(V)<3:return (frozenset(),)
 a,b=V[0],V[-1];out=set()
 for z in range(1,len(V)-1):
  k=V[z];left=V[:z+1];right=V[z:];extras={x for x in (diag(a,k,P),diag(k,b,P)) if x is not None}
  for L in triangulations(left,P):
   for R in triangulations(right,P):out.add(frozenset(set(L)|set(R)|extras))
 return tuple(out)
def catalan(q):
 import math
 return math.comb(2*q,q)//(q+1)
rows=[]
for m in range(2,7):
 P=m+3;T=triangulations(tuple(range(1,P+1)),P);edges={}
 for i,A in enumerate(T):edges[i]={j for j,B in enumerate(T) if len(A^B)==2}
 bases=set()
 for A in T:
  for base in itertools.combinations(sorted(A),m-2):bases.add(frozenset(base))
 face_counts=[];cycles_ok=True
 for base in bases:
  ids=[i for i,A in enumerate(T) if base<=A];face_counts.append(len(ids));cycles_ok &= len(ids) in (4,5) and all(len(edges[i]&set(ids))==2 for i in ids)
 rows.append({'type':f'A_{m}','polygon_vertices':P,'clusters':len(T),'catalan_expected':catalan(m+1),'flip_degree':m,'all_cluster_degrees_correct':all(len(v)==m for v in edges.values()),'rank_two_faces':len(bases),'square_faces':face_counts.count(4),'pentagon_faces':face_counts.count(5),'all_rank_two_faces_are_cycles_4_or_5':cycles_ok})
checks={'cluster_count_is_catalan':all(x['clusters']==x['catalan_expected'] for x in rows),'every_cluster_has_m_mutations':all(x['all_cluster_degrees_correct'] for x in rows),'all_rank_two_coherence_faces_are_squares_or_pentagons':all(x['all_rank_two_faces_are_cycles_4_or_5'] for x in rows),'pentagons_present_at_every_rank':all(x['pentagon_faces']>0 for x in rows),'commuting_squares_present_from_rank_three':all(x['square_faces']>0 for x in rows if int(x['type'][2:])>=3)}
out={'schema':'marici.nima.nnmhv-associahedral-coherence-faces.v1','rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'Every ambiguity between two history-cluster mutations is resolved by a square (independent flips commute) or a pentagon (overlapping flips satisfy associator coherence). These are exactly the 2-faces of the type-A associahedron.','bridges':['Mac Lane pentagon coherence','commuting-square/Beck-Chevalley coherence','cluster mutation exchange graph','associahedral higher category structure','parenthesization of composite constructions']};p=ROOT/'research/nima/results/nnmhv-associahedral-coherence-faces.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'rows':rows,'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
