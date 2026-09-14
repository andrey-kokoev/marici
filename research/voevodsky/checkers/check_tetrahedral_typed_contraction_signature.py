#!/usr/bin/env python3
"""Exact order-complex test for the local typed contraction signature."""
import hashlib,json,platform
from fractions import Fraction
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/tetrahedral_typed_contraction_signature.v1.json';OUT=ROOT/'research/voevodsky/results/tetrahedral_typed_contraction_signature.json';D=json.loads(FIX.read_text())
def pop(x):return x.bit_count()
def subsets(include_bulk=True):return [m for m in sorted(range(1,16),key=lambda x:(pop(x),x)) if include_bulk or m!=15]
def simplices(include_bulk=True):
 p=subsets(include_bulk);out={}
 for k in range(4):
  out[k]=[c for c in combinations(p,k+1) if all((c[i]&c[i+1])==c[i] and c[i]!=c[i+1] for i in range(k))]
 return out
def boundary(dom,cod):
 idx={x:i for i,x in enumerate(cod)};a=[[Fraction(0) for _ in dom] for _ in cod]
 for j,s in enumerate(dom):
  for i in range(len(s)):a[idx[s[:i]+s[i+1:]]][j]+=(-1)**i
 return a
def rank(a):
 if not a:return 0
 a=[r[:] for r in a];r=0
 for c in range(len(a[0])):
  q=next((i for i in range(r,len(a)) if a[i][c]),None)
  if q is None:continue
  a[r],a[q]=a[q],a[r];z=a[r][c];a[r]=[x/z for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][c]:z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
  r+=1
 return r
def audit(include_bulk):
 s=simplices(include_bulk);ds={k:boundary(s[k],s[k-1]) for k in range(1,4) if s[k]};betti=[]
 for k in range(4):
  if not s[k]:break
  betti.append(len(s[k])-(rank(ds[k]) if k in ds else 0)-(rank(ds[k+1]) if k+1 in ds else 0))
 return s,betti
full,bfull=audit(True);bdry,bbdry=audit(False);flags=full[3]
# Chamber adjacency: maximal flags differing in exactly one member.
adj={f:set() for f in flags}
for a,b in combinations(flags,2):
 if len(set(a)^set(b))==2:adj[a].add(b);adj[b].add(a)
seen={flags[0]};stack=[flags[0]]
while stack:
 for x in adj[stack.pop()]:
  if x not in seen:seen.add(x);stack.append(x)
expected=D['expected'];checks={'typed_four_vertices':len(D['vertex_order'])==4 and len(D['variance'])==4,'opposite_variance_pairs':D['variance']['S']==D['variance']['R']=='positive' and D['variance']['Sdual']==D['variance']['Rdual']=='negative','cell_count':len(full[0])==expected['cells'],'complete_schedule_count':len(flags)==expected['complete_schedules'],'complete_schedule_graph_connected':len(seen)==len(flags),'barycentric_f_vector':[len(full[k]) for k in range(4)]==expected['barycentric_f_vector'],'completed_betti':bfull==expected['completed_betti'],'unfilled_boundary_betti':bbdry==expected['unfilled_boundary_betti'],'bulk_boundary_oriented':D['bulk']['boundary']=='F1-F2+F3-F4'}
out={'schema':'marici.voevodsky.tetrahedral-typed-contraction-signature-check.v1','passed':all(checks.values()),'checks':checks,'observed':{'complete_schedules':len(flags),'schedule_graph_edges':sum(map(len,adj.values()))//2,'completed_f_vector':[len(full[k]) for k in range(4)],'completed_betti':bfull,'unfilled_boundary_f_vector':[len(bdry[k]) for k in range(3)],'unfilled_boundary_betti':bbdry},'disposition':'The incidence candidate has 24 connected complete schedules and contractible completed nerve; deleting the bulk leaves the expected degree-two obstruction. Source-derived map typing remains open.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_tetrahedral_typed_contraction_signature.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
