#!/usr/bin/env python3
"""Verify the face-poset duality P4 boundary ↔ Sd(tetrahedral boundary)."""
import hashlib,json,platform
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/permutohedron_tetrahedral_subdivision_duality.v1.json';OUT=ROOT/'research/voevodsky/results/permutohedron_tetrahedral_subdivision_duality.json';D=json.loads(FIX.read_text());E=D['expected']
def partitions(k):
 out=[]
 for word in product(range(k),repeat=4):
  if set(word)!=set(range(k)):continue
  out.append(tuple(tuple(i for i,x in enumerate(word) if x==j) for j in range(k)))
 return out
def chain(p):
 acc=0;out=[]
 for block in p[:-1]:
  for i in block:acc|=1<<i
  out.append(acc)
 return tuple(out)
def merge(p,i):return p[:i]+(tuple(sorted(p[i]+p[i+1])),)+p[i+2:]
parts={k:partitions(k) for k in (2,3,4)};allp=sum(parts.values(),[]);image={p:chain(p) for p in allp}
# Adjacent swaps of permutations and shared walls of maximal flags.
schedules=parts[4];schedule_set=set(schedules);edges=set();wall_ok=True
for p in schedules:
 perm=tuple(b[0] for b in p)
 for i in range(3):
  q=list(perm);q[i],q[i+1]=q[i+1],q[i];q=tuple((x,) for x in q)
  edge=frozenset((p,q));edges.add(edge)
  wall_ok &= len(set(image[p])&set(image[q]))==2
# Exhaustive cover-incidence reversal: adjacent block merge removes one chain vertex.
covers=[];incidence_ok=True
for k in (3,4):
 for p in parts[k]:
  for i in range(k-1):
   q=merge(p,i);covers.append((p,q));incidence_ok &= set(image[q])<set(image[p]) and len(image[p])==len(image[q])+1
# Facets and their schedule counts.
facets=parts[2];facet_sizes=[]
for f in facets:
 I=set(f[0]);facet_sizes.append(sum(set(tuple(b[0] for b in p)[:len(I)])==I for p in schedules))
squares=sum(x==4 for x in facet_sizes);hexagons=sum(x==6 for x in facet_sizes)
# Simplices are exactly chains obtained from ordered partitions.
simplices=set(image.values());unique=len(simplices)==len(allp)
sd_boundary_f=[len(parts[2]),len(parts[3]),len(parts[4])];p_boundary_f=[len(parts[4]),len(edges),len(parts[2])]
# Cone construction: one full-set vertex plus every boundary simplex joined to it.
bydim={0:{(15,)}}
for s in simplices:
 bydim.setdefault(len(s)-1,set()).add(s);bydim.setdefault(len(s),set()).add(s+(15,))
sd_bulk_f=[len(bydim[d]) for d in range(4)]
checks={'ordered_partition_to_chain_bijective':unique,'all_cover_incidences_reversed':incidence_ok,'schedule_count':len(schedules)==E['schedules'],'adjacent_swap_edge_count':len(edges)==E['adjacent_swap_edges'],'every_adjacent_swap_is_shared_wall':wall_ok,'proper_subset_facet_count':len(facets)==E['proper_nonempty_subsets'],'square_facet_count':squares==E['square_facets'],'hexagonal_facet_count':hexagons==E['hexagonal_facets'],'dual_boundary_f_vectors':p_boundary_f==E['permutohedron_boundary_f_vector'] and sd_boundary_f==E['subdivided_boundary_f_vector'],'full_set_cone_f_vector':sd_bulk_f==E['subdivided_bulk_f_vector']}
out={'schema':'marici.voevodsky.permutohedron-tetrahedral-subdivision-duality-check.v1','passed':all(checks.values()),'checks':checks,'observed':{'ordered_partition_cells':{str(k):len(parts[k]) for k in parts},'cover_incidences':len(covers),'facet_schedule_sizes':{'four':squares,'six':hexagons},'permutohedron_boundary_f_vector':p_boundary_f,'subdivided_boundary_f_vector':sd_boundary_f,'subdivided_bulk_f_vector':sd_bulk_f},'disposition':'The boundary cell poset of P4 is anti-isomorphic to the simplex poset of Sd(boundary Delta3); the full-set cone recovers Sd(Delta3). Semantic transport remains unproved.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_permutohedron_tetrahedral_subdivision_duality.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
